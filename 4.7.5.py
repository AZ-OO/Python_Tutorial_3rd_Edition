"""
4.7.5 Lambda(ラムダ)式
"""
# キーワード lambdaを使うと小さな無名関数が書ける。
def make_incremenor(n):
    return lambda x: x + n


f = make_incremenor(42)
print(f)
f(0)

# 用途としては、小さな関数を引数として渡すことができる
pairs = [(1,'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)
