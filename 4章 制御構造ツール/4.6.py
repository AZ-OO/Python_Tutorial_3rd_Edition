"""
4.6 関数の定義
"""

# フィボナッチ級数を似にの上限まで書き出す関数
def fib(n): # フィボナッチ級数をnまで書き出す
    """nまでフィボナッチ級数を表示する"""
    a,b = 0,1
    while a < n:
        print(a,end="")
        a,b = b, a+b
        print()
# 関数呼び出し
 fib(2000)

# リネーム
f = fib
f(100)

 # Return文を持たない関数では、Noneが返ってくる
fib(0)
print(fib(0))

# フィボナッチの要素を表示する代わりに、そのリストを返す関数
def fib2(n): # nまでのフィボナッチを書き出す
    """nまでフィボナッチからなるリストを返す"""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result

f100 = fib2(100) # コールする
print(f100)
