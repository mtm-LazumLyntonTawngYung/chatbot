# chat_controller.py
import connexion
from openapi_server.models.chat_request import ChatRequest  # noqa: E501
from openapi_server.models.chat_respond import ChatRespond  # noqa: E501
from openapi_server.services.chat_services import ChatServices


def reply_chat_case(body=None):  # noqa: E501

    if connexion.request.is_json:
        chat_request = ChatRequest.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        response_message = ChatServices.generate_chat_response(chat_request)

        chat_respond = ChatRespond(message=response_message)
        return chat_respond

    except ValueError as e:
        error_message = f"Error: {str(e)}"
        chat_respond = ChatRespond(message=error_message)
        return chat_respond, 400

    except Exception as e:
        error_message = f"Internal Server Error: {str(e)}"
        chat_respond = ChatRespond(message=error_message)
        return chat_respond, 500
