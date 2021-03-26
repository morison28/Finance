import configparser
import logging

from api import Bybit


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    conf = configparser.ConfigParser()
    conf.read('../../../../data/bot/settings.ini')
    api_key = conf['bybit']['api_key']
    api_secret = conf['bybit']['api_secret']

    bybit = Bybit(api_key, api_secret)
    