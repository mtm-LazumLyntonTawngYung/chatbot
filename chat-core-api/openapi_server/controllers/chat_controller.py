# chat_controller.py
import connexion
from openapi_server.models.chat_request import ChatRequest  # noqa: E501
from openapi_server.models.chat_respond import ChatRespond  # noqa: E501
from openapi_server.services.chat_services import ChatServices


def reply_chat_case(body=None):  # noqa: E501

    if connexion.request.is_json:
        chat_request = ChatRequest.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        # Only the part that can raise an error goes here
        response_message = ChatServices.generate_chat_response(chat_request)
    except ValueError as err:
        error_message = f"Error: {str(err)}"
        return ChatRespond(message=error_message), 400
    except Exception as err:
        error_message = f"Internal Server Error: {str(err)}"
        return ChatRespond(message=error_message), 500

    # Everything else is outside the try block
    chat_respond = ChatRespond(message=response_message)
    return chat_respond
