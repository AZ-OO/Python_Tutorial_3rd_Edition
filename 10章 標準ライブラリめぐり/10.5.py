"""
10.5 文字列パターンマッチング
"""
# reモジュールは高度な文字列処理を行う正規表現ツールを提供する
# 正規表現は複雑なマッチングや操作に簡潔で最適化された解を与える。

import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')) # <-- ['foot', 'fell', 'fastest']

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))# <-- cat in the hat

# 感嘆なことしかしないときは、文字列メソッドの方がよい。読みやすくてデバックしやすい
print('tea for too'.replace('too', 'two')) # <-- tea for two
