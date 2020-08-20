"""
9.3.5 クラス変数とインスタンス変数
"""
class Dog:
    kind = 'canine' # どのインスタンスも持つことになるクラス変数

    def __init__(self, name):
        self.name = name # インスタンスごとに固有のインスタンス変数

d = Dog('Fibo')
e = Dog('Buddy')
print(d.kind) # すべてのいうに共通
print(e.kind) # すべてのいうに共通
print(d.name) # dに固有
print(e.name) # eに固有
