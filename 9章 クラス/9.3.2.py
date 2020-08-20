"""
9.3.2 クラスオブジェクト
"""

class MyClass():
    """
    A simple example class
    """
    def __init__(self): # 初期化
        self.data = []
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass # インスタンス生成
print(x.i)
print(x.f(x))
print(x.__doc__)

# --init__()メソッドに引数を与える
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r)
print(x.i)
