"""
4.7.2 キーワード引数
"""

# 関数はキーワード引数もとれる
# 『キーワード = 値』のかたち
def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print("This parrot wouldn't", action, end = '')
    print("if you put", voltage, "volts through it.")
    print(" -- Lovery plumage, the", type)
    print(" -- It's", state, "!")

#parrot(1000) # 位置引数1個
#parrot(voltage = 1000)                                 # キーワード引数1個
#parrot(voltage = 1000000, action = 'V00000M')          # キーワード引数2個
#parrot(action = 'V00000M', voltage = 1000000)          # キーワード引数2個
#parrot('a million', 'bereft of life', 'jump')          # キーワード引数3個
#parrot('a thousand', state = 'pushing up the daisies') # 位置引数1個キーワード引数1個

# 関数をコールする時は、必ず位置引数が先でキーワード引数を後にしなければなｒない
# キーワード引数は全て関数定義の仮引数に書いたものと一致している必要があるが、その順序は問われない

#parrot()                      # 必要な引数がない
#parrot(voltage = 5.0, 'dead') # キーワード引数の後に非キーワード引数
#parrot(110,voltage = 200)     # 同じ引数に値を2度与えた
#parrot(actor = 'John Cleese') # 未知のキーワード引数

# 仮引数の最後が**名前の形になっていると、この引数はディクショナリを受け取る
# このディクショナリには、仮引数に対応するキーワードを除いたすべてのキーワード引数が入っている
# つまり、この形にすればカリヒキスにないキーワードが使える
# またこれは、*名前の形式と組み合わせて使うことができる
# この形式では、仮引数にない位置指定型引数を全て含んだタプルが関数に渡る

def chessshop(kind, * arguments, **keywords):
    print('-- Do you have any', kind, '?')
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw,':', keywords[kw])

chessshop("Limburger", "It's very runny sir.",
         "It's really very, VERY runny, sir.",
         shopkeeper = "Mihael Palin",
         client = 'John Cleese',
         sketch = 'Cheese SHop Sketch')
