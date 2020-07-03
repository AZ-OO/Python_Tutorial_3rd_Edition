"""
4.7.1 引数のデフォルト値
"""

# 一番使いでがある形態は、いくつかの引数にデフォルト値を設定するというもの
# これを使った関数は、渡すように定義してあるよりお少ない個数の引数でコールできる
def ask_ok(prompt, retrise = 4, complaint = 'Yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retrise = retrise - 1
        if retrise < 0:
            raise OESError('非協力的なユーザー')
        print(complaint)

# 必須の引数だけを与える
#ask_ok ('Do you really want to quit?')

# オプション引数を1つ与える
#ask_ok('OK to overwrite the file?', 2)

# すべての引数を与える
#ask_ok('Ok to overwrite the ile?', 2, 'Come on, only yes or no!')

# デフォルト値の評価は一度しかおきない
i=5
def f(arg = i):
    print(arg)

i = 6
# f()

# コールで渡されるひきすうを累積していく
def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# コール間で、デフォルト値を共有されたくないなら、こう書く
def f2(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))
