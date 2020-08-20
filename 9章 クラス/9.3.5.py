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

# すべてのDogインスタンスでただ1つのリストが共有されてしまう
class Dog2:

    tricks = [] # クラス変数の使い方を間違えている

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
d2 = Dog2('Fido2')
e2 = Dog2('Buddy2')
d2.add_trick('ころがる')
e2.add_trick('死んだふり')
print(d2.tricks) # すべての犬が共有しているなんて！

class Dog3:

    def __init__(self, name):
        self.name = name
        self.tricks = [] # それぞれの犬に新たに空リストを生成

    def add_trick(self, trick):
        self.tricks.append(trick)

d3 = Dog3('Fido3')
e3 = Dog3('Buddy3')
d3.add_trick('ころがる')
e3.add_trick('死んだふり')
print(d3.tricks)
print(e3.tricks)
