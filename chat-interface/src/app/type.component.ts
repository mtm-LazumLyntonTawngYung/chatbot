export interface ChatMessage {
    message: string;
    role: MsgSender;
  }
  
  export interface RequestMsg {
    bot_style: BotStyle;
    message: string;
    messages: ChatMessage[]
  }
  
  export interface RespondMsg {
    message: string;
  }
  
  export interface BotMsg {
    greetingMsg: string;
    questionMsg: string;
    nextQAMsg: string;
    defaultMsg: string;
  }
  
  export enum MsgSender {
    system = 'system',
    bot = 'bot',
    user = 'user'
  }
  
  export enum BotStyle {
    normal = 'normal',
    friend = 'friend',
    doctor = 'doctor'
  }