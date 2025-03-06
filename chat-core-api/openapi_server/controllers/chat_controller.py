import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.chat_request import ChatRequest  # noqa: E501
from openapi_server.models.chat_respond import ChatRespond  # noqa: E501
from openapi_server import util


def reply_chat_case(chat_request):  # noqa: E501
    """Respond to a chat case

    Allow user to send message and receive response from chatbot based on the personas # noqa: E501

    :param chat_request: 
    :type chat_request: dict | bytes

    :rtype: Union[ChatRespond, Tuple[ChatRespond, int], Tuple[ChatRespond, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        chat_request = ChatRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
