import { Component } from '@angular/core';
import { ChatInterfaceComponent } from './pages/chat-interface/chat-interface.component';

@Component({
  selector: 'app-root',
  imports: [ChatInterfaceComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'chat-interface';
}
