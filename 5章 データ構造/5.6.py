"""
5.6 ループのテクニック
"""

# ディクショナリにループをかけるとき、items()メソッドを使えばキーとそれに対応した値を同時に得られる

knight = {'gallahad' : 'the pure', 'robin' : 'the brave'}
for k,v in knight.items():
    print(k,v)


# シーケンスにループをかけるとき、enumerate()関数を使うと位置インデックスとそれに対応した値を同時に得ることができる
for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 2つ以上のシーケンスに同時にループをかけるときは、zip()関数を使うと両者のエントリをペアにできる
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q,a))

# シーケンスを逆順にループするには、まずシーケンスを正順で指定し、これにreversed()関数をコールする
for i in reversed(range(1, 10, 2)):
    print(i)

# シーケンスをソート順にループするにｈsorted()関数を使う。
# この関数は基のシーケンスに触らず、新たにソート済のリストを返す
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# リスト中のリストを改変したい要求はときにはあるものだが、新しいリストを作った方が簡単で安全
import math
raw_date = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_date:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
