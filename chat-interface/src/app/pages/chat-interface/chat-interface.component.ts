import { Component, OnInit, ViewChild, ElementRef, CUSTOM_ELEMENTS_SCHEMA, AfterViewChecked } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzAvatarModule } from 'ng-zorro-antd/avatar';
import { NzRadioModule } from 'ng-zorro-antd/radio';
import { NzTypographyModule } from 'ng-zorro-antd/typography';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzIconModule } from 'ng-zorro-antd/icon';

import { LoadingComponent } from '../../loading/loading.component';
import { ChatService } from '../../chat.service';
import { appConstants } from '../../constants/appConstants';
import { BotStyle, BotMsg, ChatMessage, MsgSender } from '../../type.component';
import { MessageComponent } from '../../message/message.component';

@Component({
  selector: 'app-chat-interface',
  imports: [
    NzLayoutModule,
    NzAvatarModule,
    NzRadioModule,
    NzTypographyModule,
    NzCardModule,
    LoadingComponent,
    CommonModule,
    FormsModule,
    NzInputModule,
    NzIconModule,
    MessageComponent,
  ],
  templateUrl: './chat-interface.component.html',
  styleUrl: './chat-interface.component.css',
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ChatInterfaceComponent implements OnInit, AfterViewChecked{
  @ViewChild('chatWindow') private chatWindow!: ElementRef;
  isLoading = false;
  messages: ChatMessage[] = [];
  userInput = '';
  isComposing = false;
  botStyle = appConstants.BOT_STYLE;
  selectedRadioOption: BotStyle = BotStyle.normal;

  constructor(private chatService: ChatService){}

  ngOnInit(): void {
    this.handleBotChanged();
  }

  ngAfterViewChecked(): void {
    this.scrollToBottom();
  }

  handleBotChanged(): void{
    this.messages = [];
    const chatMsg = this.getChatMsgWithBot(this.selectedRadioOption);
    this.initiateMessage(chatMsg.greetingMsg);
    this.initiateMessage(chatMsg.questionMsg)
  }

  getChatMsgWithBot(botStyle: BotStyle): BotMsg {
    return appConstants.CHAT_MSG[botStyle as keyof typeof appConstants.CHAT_MSG];
  }

  

  onCompositionStart(): void{
    this.isComposing=true;
  }

  onCompositionEnd(): void{
    this.isComposing=false;
  }

  initiateMessage(textMsg: string): void{
    this.isLoading = true;
    setTimeout(() =>{
      this.isLoading = false;
      this.messages.push({
        message: textMsg, role: MsgSender.bot
      });
    }, appConstants.TIME_OUT_SETTING);
    this.scrollToBottom();
  }

  private scrollToBottom(): void {
    try {
      if (this.chatWindow && this.chatWindow.nativeElement) {
        this.chatWindow.nativeElement.scrollTop = this.chatWindow.nativeElement.scrollHeight;
      }
    } catch (err) {
      console.error('Scroll to bottom failed:', err);
    }
  }
  

  

  handleInputMsg(event: KeyboardEvent): void{
    if (event.key === 'Enter' && !this.isComposing){
      this.sendMessage();
    }
  }

  sendMessage(): void {
    if (this.userInput.trim() && !this.isLoading) {
      this.messages.push({
        message: this.userInput.trim(),
        role: MsgSender.user
      });
      this.userInput = '';
      this.replyMessage(this.userInput.trim());
    }
  }

  replyMessage(textMsg: string): void {
    const botResponse = this.chatService.getChatMessageReply(this.selectedRadioOption, textMsg);
    this.isLoading = true;
    setTimeout(() => {
      this.isLoading = false;
      this.messages.push({
        message: botResponse.message,
        role: MsgSender.bot
      });
    }, 1000);
  }
  
}
