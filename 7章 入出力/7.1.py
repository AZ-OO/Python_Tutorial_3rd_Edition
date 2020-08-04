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

# str.format()メソッドで、キーワードを引数に鳥、参照にこのキーワードを使うことができる
print('This {food} is {Adjective}.'.format(food = 'spam', Adjective = 'Absolutely horrible'))

# 位置引数とキーワード引数は自由に混在できる
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other = 'Georg'))

# 『！a』(ascii()を適用)、『！s』(str()を適用)、『！r』(rept()を適用)を使えばフォーマット前に値の変換ができる
import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

# フィールドの後ろには、『:』とそれに続くフォーマット指定子をついあkすることもできる
# これにより値のフォーマットは更にコントロールしやすくなる

# πを小数点以下3文字に丸める
print('πの値はおよそ{0:.3f}である。'.format(math.pi))

# 『:』の後に整数を渡せばフィールドの文字数の最小幅が指定できる
# これは、表を綺麗に仕上げるのに役立つ
table = {'Sjoerd':4127, 'Jack':4098, 'Dcab':7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

# 非常に長い分割したくないフォーマット文字列があるんら、変数は位置ではなく名前で参照できたほうが嬉しい
# これはdictを渡してアクセスキーに角カッコ([])を使うだけで可能
table = {'Sjoerd': 4127, 'jack':4098, 'Dcab':8637678}
print('jack:{0[jack]:d}; Sjoerd:{0[Sjoerd]:d}; '
      'Dcab:{0[Dcab]:d}'.format(table))

# tableを**表記を使ってキーワード引数として渡しても同じことができる
table = {'Sjoerd': 4127, 'jack':4098, 'Dcab':8637678}
print('jack:{jack:d}; Sjoerd:{Sjoerd:d}; '
      'Dcab:{Dcab:d}'.format(**table))

# 文字列のフォーマッティングには、%演算子を使うこともできる
# これはsprintf()で使われるのとほぼ同じ形式をとった左辺引数を解釈し、
# 右辺引数に適用する
print(('πの値はおよそ%5.3fである。' % math.pi))
