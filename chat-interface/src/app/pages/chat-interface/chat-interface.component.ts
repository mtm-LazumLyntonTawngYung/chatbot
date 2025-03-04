import { Component, OnInit, ViewChild, ElementRef, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
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
import { BotStyle, BotMsg, RequestMsg, ChatMessage, RespondMsg, MsgSender } from '../../type.component';
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
    MessageComponent
  ],
  templateUrl: './chat-interface.component.html',
  styleUrl: './chat-interface.component.css',
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ChatInterfaceComponent implements OnInit{
  @ViewChild('chatWindow') chatWindow: ElementRef | null = null;
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

  handleBotChanged(): void{
    this.messages = [];
    const chatMsg = this.getChatMsgWithBot(this.selectedRadioOption);
    this.initiateMessage(chatMsg.greetingMsg);
    this.initiateMessage(chatMsg.questionMsg)
  }

  getChatMsgWithBot(botStyle: BotStyle): BotMsg {
    return appConstants.CHAT_MSG[botStyle as keyof typeof appConstants.CHAT_MSG];
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

  onCompositionStart(): void{
    this.isComposing=true;
  }

  onCompositionEnd(): void{
    this.isComposing=false;
  }

  scrollToBottom(): void {
    if (this.chatWindow) {
      setTimeout(() => {
        window.scrollTo({
          top: this.chatWindow?.nativeElement.clientHeight,
          behavior: 'smooth'
        });
      }, appConstants.TIME_OUT_SETTING);
    }
  }

  handleInputMsg(event: KeyboardEvent): void{
    if (event.key === 'Enter' && !this.isComposing){
      this.sendMessage();
    }
  }

  sendMessage(): void{
    if (this.userInput.trim() && !this.isLoading){
      this.messages.push({
        message: this.userInput.trim(), role: MsgSender.user
      });
      this.scrollToBottom();
      this.replyMessage(this.userInput.trim());
      this.userInput='';
    }
  }

  getMessageClass(message: any): string{
    return message.role === 'bot' ? 'user' : 'bot';
  }

  replyMessage(textMsg: string): void {
    const botResponse = this.chatService.getChatMessageReply(this.selectedRadioOption, textMsg);
    
    setTimeout(() => {
      this.isLoading = false;
      this.messages.push({
        message: botResponse.message,
        role: MsgSender.bot
      });
      this.scrollToBottom();
    }, appConstants.TIME_OUT_SETTING);
  }
  
}
