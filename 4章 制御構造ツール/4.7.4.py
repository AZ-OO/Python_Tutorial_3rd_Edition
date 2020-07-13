"""
4.7.4 引数リストのアンパック
"""

# 引数にしたいものがすでにリストやタプルになっていて、
# 位置してい型行き数を要求する関数のためにアンパックしなければならないという時
print(list(range(3,6)))

args = [6,10]
print(list(range(*args)))

def parrot(voltage, state = 'a stiff', action = 'voom'):
    print("This parrot wouldn't", action, end= ' ')
    print("if you put", voltage, 'volts through it.', end = ' ')
    print("E's", state, '!')
d = {"voltage":'four million', "state":"bleedin' demised", 'action':'VOOM'}
print(parrot(**d))
