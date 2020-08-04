"""
7.1 手の込んだ出力フォーマット
"""

# str(object)は、objectをユーザーが読みやすい文字列に変換して返す。
# エンドユーザーに出力する。
#repr(object)は、objectをeval()で再び元のオブジェクトに戻せる文字列に変換して返す。representationの略。
# デバッグ用に出力する。
s = 'Hello, World.'
print(str(s))
print(repr(s))

import datetime
today = datetime.date.today()
print(str(today))  # <-- todayが文字列なのか、dateオブジェクトなのか見分けがつきません。
 # 2020-07-30のようなカタチで出力
print(repr(today)) # <-- はtodayがdatetime.dateオブジェクトであることがわかる
# datetime.date(2020, 7, 30)のようなカタチで出力

print(str(1/7))
print(repr(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ' and y is ' + repr(y) + '...'
print(s)
# 文字列のrepr()は文字列クォートとバックスラッシュを追加する
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# あらゆるPythonオブジェクトがrepr()の引数になれる
print(repr((x, y, ('spam', 'eggs'))))

# 2種類の方法で平方と立方の表を書く
for x in range(1, 11):
    # str.rjust()メソッドで、文字列の左側にスペースを追加して指定の幅に右揃えする
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 上の行でendを使っていることに注目
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# str.zfill()メソッドで、数字の文字列の左側をゼロパディングする
print('12'.zfill(5))            # <-- 00012
print('-3.14'.zfill(7))         # <-- -003.14
print('3.14159265359'.zfill(5)) # <-- 3.14159265359

# str.format
# 中【】とその中の文字(これらをフォーマットフィールドという)は、
# str.format()メソッドに渡されたオブジェクトで置き換えられる。
# 中カッコの中には、str.formt()メソッドに渡されたオブジェクトの位置を参照する数字を入れる事もできる。
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

