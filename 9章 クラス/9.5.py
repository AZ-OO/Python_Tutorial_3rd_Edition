"""
9.5 継承
"""

class base():
    def a(self):
        print('私の名前はbase.aです。base.bをコールします')
        self.b()
    def b(self):
        print('私の名前はbase.bです。der.bでオーバーライドされます')

class der(base):
    def b(self):
        print('ウヒョ！ オイラはder.bだよ。')

b = base()
d = der()
b.a()
d.a()
