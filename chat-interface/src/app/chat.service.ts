import { Injectable } from '@angular/core';
import { BotMsg, BotStyle, RespondMsg } from './type.component';
import { appConstants } from './constants/appConstants';

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  getChatMessageReply(botStyle: BotStyle): RespondMsg {
    const botMsg: BotMsg = appConstants.CHAT_MSG[botStyle as keyof typeof appConstants.CHAT_MSG];
    
    return { message: botMsg.defaultMsg || appConstants.DEFAULT_MSG };
  }
}



