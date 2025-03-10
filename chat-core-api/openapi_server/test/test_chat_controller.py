import unittest

from flask import json

from openapi_server.test import BaseTestCase


class TestChatController(BaseTestCase):
    """ChatController integration test stubs"""

    def test_reply_chat_case(self):
        """Test case for reply_chat_case

        Respond to a chat case
        """
        chat_request = {"bot_style": "normal", "messages":
                        [{"role": "user", "message":
                          "私はよく薬を飲むのを忘れてしまいます。"}, {
                            "role": "user", "message":
                            "私はよく薬を飲むのを忘れてしまいます。"}],
                        "message": "私はよく薬を飲むのを忘れてしまいます。"}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/v1/chat/case',
            method='POST',
            headers=headers,
            data=json.dumps(chat_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
