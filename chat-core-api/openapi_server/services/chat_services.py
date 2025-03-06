
class ChatServices:
    def generate_chat_response(chat_request):
        """
        Generates a response from the chatbot based on the provided chat request.

        :param chat_request: The chat request from the user.
        :return: A response message based on the bot style.
        """
        # Extract information from the chat_request
        bot_style = chat_request.bot_style
        message = chat_request.message

        # Define responses for different bot styles
        responses = {
            'normal': "薬を定期的に服用することは重要です。毎日のリマインダーを設定すると役立つかもしれません。",
            'friend': "大丈夫です、忘れた時は一緒にリマインダーをセットしようね。",
            'doctor': "薬を飲み忘れると健康に影響を及ぼす可能性があります。リマインダーを使って忘れないようにしましょう。"
        }

        # Generate a response based on the bot style
        if bot_style not in responses:
            raise ValueError(f"Unsupported bot style: {bot_style}")

        response_message = responses[bot_style]

        return response_message
