"""
5.1.3 リスト内包
"""

# リスト内包はリストを生成する簡潔な方法を提供する
# よくあつ使い方として、シーケンスや反復可能体のメンバそれぞれになんらかの処理を加えて新しいリストを生成したり、
# ある条件にかなう要素のみを取り出してサブシーケンスを姿勢する

squares = []
for x in range(10):
    squares.append((x**2))
print(squares)

# 以下の方法を使えば、副作用ないに2乗数のリストを作る事ができる
squares2 = []
squares2 = list(map(lambda x : x**2, range(10)))
print(squares2)

# 以下も対等な方法
squares3 = []
squares3 = [x**2 for x in range(10)]
print(squares3)

# リスト内包とは、式とそれに続くfor節から成り、さらに0個医女のfor節やif節を後ろに続け、
# 全体を大カッコ([])で囲んだもの
# 得られるものは、最初の式を接続のfor節やif節の文脈で評価した値による新しいリストである

# 2つのリストから要素を取り、両者が同一でなけｒばタプルにまとめる
tp = []
tp = [(x,y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]
print(tp)

# 以下は、上記と等価である
combs = []
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
# 値を2倍にした新しいリストを生成
vec2 = [x * 2 for x in vec]
print(vec2)

# 負の数を除去するようにフィルタを書ける
vec3 = [x for x in vec if x >= 0]
print(vec3)

# すべての要素に関数を適用
vec4 = [abs(x) for x in vec]
print(vec4)

# 各要素にメソッド(前後の空白を除去)をコール
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
vec5 = [weapon.strip() for weapon in freshfruit]
print(vec5)

# 2個のタプル(数値、2乗値)のリストを生成
vec6 = [(x, x**2) for x in range(6)]
print(vec6)

# タプルを丸カッコで囲わないとエラーになる
# vec7 = [x, x**2 for x in range(6)]
# print(vec7)

# File "<stdin>", line 1, in ?
#     [x, x**2 for x in range(6)]

# forを2つ使ってリストを平準化(1次元化)する
vec8 = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
vec9 = [num for elem in vec8 for num in elem]
print(vec9)

# リスト内包には複合式や入れ子の関数を含むことができる
from math import pi
vec10 = [str(round(pi, i)) for i in range(1, 6)]
print(vec10)
