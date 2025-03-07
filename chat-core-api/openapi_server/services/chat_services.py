
class ChatServices:
    def generate_chat_response(chat_request):
        bot_style = chat_request.bot_style

        responses = {
            'normal': "薬を定期的に服用することは重要です。毎日のリマインダーを設定すると役立つかもしれません。",
            'friend': "大丈夫です、忘れた時は一緒にリマインダーをセットしようね。",
            'doctor': "薬を飲み忘れると健康に影響を及ぼす可能性があります。リマインダーを使って忘れないようにしましょう。"
        }

        if bot_style not in responses:
            raise ValueError(f"Unsupported bot style: {bot_style}")

        response_message = responses[bot_style]

        return response_message
