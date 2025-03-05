import { Injectable } from '@angular/core';
import { BotMsg, BotStyle, RespondMsg } from './type.component';
import { appConstants } from './constants/appConstants';

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  getChatMessageReply(botStyle: BotStyle, userMessage: string): RespondMsg {
    const botMsg: BotMsg = appConstants.CHAT_MSG[botStyle as keyof typeof appConstants.CHAT_MSG];

    if(userMessage.includes('hi')){
      return { message: 'こんにちは！本日はどのようなご用件でしょうか？'};
    }
    
    return { message: botMsg.defaultMsg || appConstants.DEFAULT_MSG };
  }
}

