"""
4.3 range()関数
"""

# 数字なの連なる反復をかけるときは、range()関数が便利
# 与えられた終端値は入らない
# これは、等差級数を生成する
for i in range(5):
    print(i)

# range()が生成する値は、各アイテムのインデックスとなる
# 0以外の数字から始めることもできるし、増分(ステップとも呼ばれる)を指定することも可能
# ステップは負数も使える
for i in range(5,10):# 5から10まで
    print(i)

for i in range(0,10,3): # 0から10までで、3ずつインクリ
    print(i)

for i in range(-10,-100,-30):
    print(i)

# シーケンスのインデックスで反復をかけたいときは、次のようにrange()とlen()を組み合わせる
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])
