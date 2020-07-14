"""
5.3 タプルとシーケンス
"""
# タプルはカンマで区切られた値からなる
t = 12345,54321,'hello'
print(t[0])
print(t)

# タプルは入れ子にできる
u = t,(1, 2, 3, 4, 5)
print(u)
# タプルは変更不可
#t[0] = 88888

# しかし、変更可能オブジェクト(この場合はリスト)を格納できる
v = ([1, 2, 3], [3, 2, 1])
print(v)
v[0][1] = 5 # リストの値を変更
print(v)

# アイテム数が0や1のタプルを作る
# 空のタプル
empty = ()
# 1アイテムのタプル
singleton = 'hello', # <-- ぶら下がったカンマに注目
print(len(empty))
print(len(singleton))
print(singleton)
