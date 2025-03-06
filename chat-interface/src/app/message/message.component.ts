import { Component, Input, OnChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { ChatMessage } from '../type.component';

@Component({
  selector: 'app-message',
  imports: [
    CommonModule
  ],
  templateUrl: './message.component.html',
  styleUrl: './message.component.css'
})
export class MessageComponent implements OnChanges {
  @Input() chatMsg!: ChatMessage;
  messageContent!: SafeHtml

  constructor(private sanitizer: DomSanitizer) { }

  ngOnChanges(): void {
    this.messageContent = this.sanitizer.bypassSecurityTrustHtml(this.chatMsg?.message)
  }
}
