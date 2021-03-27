import hashlib
import hmac
import json
import logging
import threading
import time

import websocket


class Bybit(object):

    def __init__(self, api_key, api_secret, symbol):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug('Initializing WebSocket.')

        self.api_key = api_key
        self.api_secret = api_secret
        self.symbol = symbol

        self.endpoint = 'wss://stream-testnet.bybit.com/realtime'

        self.channel_list = [
            'trade.' + self.symbol, 
        ]

        self.data = {
            'connection': False,
        }

        self.__connect(TESTNET_PUBLIC)

    def __connect(self, endpoint):
        while not self.data['connection']:
            self.ws = websocket.WebSocketApp(endpoint,
                                             on_message=self.__on_message,
                                             on_close=self.__on_close,
                                             on_open=self.__on_open,
                                             on_error=self.__on_error,
                                             # header=None, # 必要？
                                            )
            self.ws_th = threading.Thread(target=lambda: self.ws.run_forever())
            self.ws_th.daemon = True
            self.ws_th.start()
            time.sleep(10)

        self.__wait_first_data
        self.logger.debug('WebSocket Opened.')

    def __wait_first_data(self):
        for i in self.data['timestamp']:
            if i in ['position', 'execution', 'order']:
                continue
            while not self.data['timestamp'][i]:
                time.sleep(1.0)

    def __exit(self):
        pass

    def __on_message(self):
        pass

    def __on_close(self):
        pass

    def __on_open(self):
        pass

    def __on_error(self):
        pass

    def send_ping(self):
        pass

    def reconnect(self):
        pass
