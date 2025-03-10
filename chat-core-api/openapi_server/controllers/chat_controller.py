# chat_controller.py
import connexion
from openapi_server.models.chat_request import ChatRequest  # noqa: E501
from openapi_server.models.chat_respond import ChatRespond  # noqa: E501
from openapi_server.services.chat_services import ChatServices


def reply_chat_case(body=None):  # noqa: E501
    if connexion.request.is_json:
        param_data = ChatRequest.from_dict(connexion.request.get_json())
        service = ChatServices()
        ret_msg = service.get_chat_respond(
            param_data.message, param_data.bot_style)
        return ChatRespond.from_dict({'message': ret_msg})
    return None
