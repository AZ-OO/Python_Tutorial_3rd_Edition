"""
9.4 その他いろいろ
"""

# クラスの外で定義された関数
def f1(self, x, y):
    return min(x, x + y)
'''
class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
    print(type(h) <-- function
'''
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
