"""
11.1 出力整形
"""

# reprlibモジュールはrepr()の別バージョンだ
# 巨大なまたは深く入れ子になったコンテナオブジェクトを省略して表示する

import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))

# pprintモジュールを使うと、ビルトインオブジェクトにもユーザー定義オブジェクトにも使える
# 洗礼された出力制御が使える。
# 出力はインタープリタが読める形になっている

import pprint

t = [[[['black', 'cyan'], 'whit', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width = 30)
# -->
'''
[[[['black', 'cyan'],
   'whit',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
'''

# textwrapモジュールは、テキストの各段落を指定のはあに納まるように整形する
import textwrap
doc = """The wrap() method is just like fill() except that it returns
         a list of strings instead of one big string with newlines to eparate
         the wrapped lines.
"""

print(textwrap.fill(doc, width = 40))
# -->
"""
The wrap() method is just like fill()
except that it returns          a list
of strings instead of one big string
with newlines to eparate          the
wrapped lines.
"""

# loacleモジュールは文化固有のデータフォーマットのデータベースにアクセスするもの
# localのformat関数にあるオブジェクト引数groupingを使うと、数値を桁区切り付きに整形できる
#import locale
#locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')
import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252') # <-- locale.Error: unsupported locale settingになってしまう
                                                              #     おそらく、local.pyに1252がないため
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') # <-- en_US.UTF-8
conv = locale.localeconv() # 慣習競っくのマッピングを取得
x = 1234567.8
print(locale.format('%d', x, grouping = True)) # <-- 1,234,567
print(locale.format_string('%s%.*f', (conv['currency_symbol'], conv['frac_digits'], x), grouping = True)) # < --$1,234,567.80