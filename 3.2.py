"""
3.2 プログラミング はじめの一歩
"""

# フィボナッチ級数の始め方
# フィボナッチとは、0、1、1、2、3、5、8、13、21、34、55、89、144、233、377…
# 0と1から始まる数列は、それ以降のどの項も直前2つの項の和になっているのが特徴
#   F0＝0(初期条件1)
# F1＝1(初期条件2)
# Fn+2＝Fn＋Fn+1（n≧0）
# フィボナッチ級数
# 2項の和により次項が定まる
a,b = 0,1 # 多重代入
while b < 10:
    print(b)
    a,b = b, a + b

# print()関数
i = 256 * 256
print('The value of i is',i)

# キーワード引数endを使えば、出力末尾の改行の制御や、出力末尾を他の文字列に変更する事ができる
a,b = 0,1
while b < 1000:
    print(b, end=',')
    a,b = b, a+b