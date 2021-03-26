import hashlib
import hmac
import json
import logging
import threading
import time

import websocket


class Bybit(object):

    def __init__(self, api_key, api_secret):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug('Initializing WebSocket.')

        self.api_key = api_key
        self.api_secret = api_secret
