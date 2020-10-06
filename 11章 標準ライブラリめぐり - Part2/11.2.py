"""
11.2 テンプレート
"""

# stringモジュールには、エントリーユーザーが編集するのに向いた構文を持つ、
# 万能のTempleteクラスがある。
# これを使えばアプリケーション自愛を書き換えずにカスタマイズできるようになる。
# 整形ではプレースホルダ(置き換え記号)の名前として、$の後ろにPythonで有効な
# 識別子を付けたものを使う。
# プレースホルダを中括弧で囲めば、スペースで区切らなくても後ろに英文字・数字を続けられる。
# $$と書けば、エスケープされたひとつの$になる。

# substituteメソッドは、プレースホルダをディックショナリかキーワード引数で渡さないと
# KeyErrorを送出する

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village = 'Nottingham', cause = 'the itch found')) # <-- Nottinghamfolk send $10 to the itch found.

# こうした置き換えスタイルのアプリケーションでは、ユーザーからのデータは不完全かもしれないので、
# safe_substituteメソッドの方が適しているかもしれない
# こちらはデータがなければプレースホルダをそのままにする

t = Template('Return the $item to $owner.')
d = dict(item = 'unlanden swallow')

# print(t.substitute(d)) # <-- Traceback (most recent call last):
                       # KeyError: 'owner'

print(t.safe_substitute(d)) # <-- Return the unlanden swallow to $owner.

# Templateのサブクラスでは区切文字(デリミタ)を変えられる。
# 例えば以下のようなフォトブラウザ向けバッチ処理リネームユーティリティでは、
# 現在の日付、画像番号、ファイル形式などのプレースホルダに%記号を使いたいかもしれない

import time, os.path
photofiles = ['img_1074,jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('どのようにリネームしますか(%d-日付 %n-番号 %f-形式):')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d = date, n = i, f = ext)
    print('{0} --> {1}'.format(filename, newname))

