

## logging
ドキュメント   
https://docs.python.org/ja/3/library/logging.html

``` python
import logging

# 例)開発時はDEBUG, 運用時はINFO
logging.basicConfig(level=logging.INFO,
                    filename='',
                    format=formatter)

# formatter
# 例) 日付，ログレベル，メッセージの出力
formatter = '%(asctime)s:%(levelname)s:%(message)s'

# 出力：format記法なども出来るが↓のようにも可
logging.info('info %s %s', 'test1', 'test2')

# ロガー
# getLoggerでファイル名を指定
# mainでloggingの設定をして，後はloggerで設定をしていくことが割と良い
logger = logging.getLogger(__name__)
logger.setLevel()
logger.info()

# ハンドラ
# 例) logging.info()はコンソール出力のみでloggerはファイルに書き出したい場合
# ハンドラーの種類
# https://docs.python.org/ja/3/library/logging.handlers.html
h = logging.FileHandler('logtest.log')
logger.addHandler(h)

# フィルター
# TODO

# ロギング コンフィグ
# TODO

# ログ解析時に便利だったりするので，key:valueでログ出力するのも良い

logger.error){
    'action': 'something',
    'status': 'faul',
    'message': 'Api call failed',
}

```
