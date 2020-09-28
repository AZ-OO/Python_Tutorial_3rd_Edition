""""
10.7 インターネットへのアクセス
"""

# さまざまなインターネットプロトコルを処理してインターネットにアクセスする、
# さまざまなモジュールがある。
# 特にシンプルなのはURLにあるデータを処理するurllib.requestと、メールを送るsmtplibだ

from urllib.request import urlopen
with urlopen('https://tycho.usno.navy.mil/cgi-bin/timer.pl') as response: # <-- URLが死んでる
    for line in response:
        line = line.decode('utf-8')        # バイナリデータをテキストにデコード
        if 'EST' in line or 'EDT' in line: # 東部標準時を探す
            print(line)
