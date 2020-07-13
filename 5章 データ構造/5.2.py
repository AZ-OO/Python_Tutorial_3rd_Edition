"""
5.2 del文
"""

# リストのアイテムを削除する再、値ではなくインデックスで指定する方法にdel文がある
# これは値をかえさないところがpop() メソッドと異なる
# del文はリストからスライスで削除したり、リスト全体の消去にも使える

a = [-1, 1, 66.25, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

# delは変数を丸ごと削除するのにも使える
b = [-1, 1, 66.25, 333, 1234.5]
print(b)
del b
