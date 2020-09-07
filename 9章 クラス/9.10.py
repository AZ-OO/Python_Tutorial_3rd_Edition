"""
9.10 ジェネレータ
"""

# ジェネレータは反復子を作るためのシンプルでパワフルなツール
# 普通の関数と同じように書くが、デーアを返す部分でyieldを使う
# next()がコールされるたびに、ジェネレータは前回抜けたところに戻る

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf')
    print(char)
