# chat_controller.py
import connexion
from openapi_server.models.chat_request import ChatRequest  # noqa: E501
from openapi_server.models.chat_respond import ChatRespond  # noqa: E501
from openapi_server.services.chat_services import ChatServices


def reply_chat_case(body=None):
    if connexion.request.is_json:
        incoming_data = ChatRequest(**connexion.request.get_json())
        service = ChatServices()
        response_message = service.get_chat_respond(
            incoming_data.message, incoming_data.bot_style)
        return ChatRespond(**{'message': response_message})
    return None
