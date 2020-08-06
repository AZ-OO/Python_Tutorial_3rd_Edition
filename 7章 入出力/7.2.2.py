"""
構造のあるデータをjsonで保存する
"""

# PythonではJSON(javaScript Object Notaition)という
# ポピュラーなデータ変換フォーマットが使える。
# 標準モジュールjsonはPythonのデータ階層構造を取って文字列表現をコンバートすることができる。
# このプロセスを『シリアライズ』という。
# 文字列表現からデータを再構築することは『デシリアライズ』という。

import json
x = [1, 'simple', 'list']
json.dumps(x)
print(x)
