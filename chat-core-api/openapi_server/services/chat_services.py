from openapi_server.variables import responses


class ChatServices:
    def generate_chat_response(chat_request):
        bot_style = chat_request.bot_style

        if bot_style not in responses:
            raise ValueError(f"Unsupported bot style: {bot_style}")

        response_message = responses[bot_style]

        return response_message
