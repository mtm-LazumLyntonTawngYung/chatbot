#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from openapi_server.variables import port

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', arguments={'title': 'Chat Core Api'}, pythonic_params=True)

flask_app = app.app


def main():
    app.run(port=port, debug=True)


if __name__ == '__main__':
    main()
