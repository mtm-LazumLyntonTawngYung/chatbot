#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from openapi_server.variables import port


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Chat Core Api'},
                pythonic_params=True)

    app.run(port=port)


if __name__ == '__main__':
    main()
