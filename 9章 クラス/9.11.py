"""
9.11 ジェネレータ式
"""
print(sum(i*i for i in range(10))) # 2乗して合計

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x, y in zip(xvec, yvec))) # 内積
