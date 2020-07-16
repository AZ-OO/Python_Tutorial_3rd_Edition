"""
5.4 集合(set)
"""

# 集合とは、重複しない要素を順不同で集めたもの
# 基本的な用途は存在判定(mambership testing)や
# 重複エントリの排除

# 集合の生成には中カッコ{}
# または set()関数を使用する
# 空の集合を生成するには{}ではなくset()を使う必要がある

brekfirst = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(brekfirst) # 重複が削除されている
print('orange' in brekfirst) # 高度な存在判定
print('crabgrass' in brekfirst)

# 2つの単語から非重複(ユニーク)文字を取って集合演算を実演
a = set('abracadabra')
b = set('alacazam')
print(a)     # aのユニーク文字
print(a - b) # aに存在いbにはない文字
print(a | b) # aまたはbに存在する文字
print(a & b) # aにもbにも存在する文字
print(a ^ b) # aまたはbにある共通しない文字

# リスト内包とよく似た集合内包もサポート
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
