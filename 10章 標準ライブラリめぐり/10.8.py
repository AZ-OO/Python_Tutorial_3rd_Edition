"""
10.8 日付と時間
"""

# datetimeモジュールは、日付と時間を簡単にも複雑にも処理できる一連のクラスを提供する
# 日付と時間の計算をサポートしつつも、実装の焦点は出力の整形や操作のために効果的に
# 要素抽出することに当てられている。
# このモジュールではタイムゾーンを意識したオブジェクトもサポートしている

# DATEオブジェクトの構築と整形は簡単だ
from datetime import date
now = date.today()
print(now) # <-- 2020-09-29
print(now.strftime('%m-%d-%y. %d %b %y is a %A on the %d day of %B.')) # <-- 09-29-20. 29 Sep 20 is a Tuesday on the 29 day of September.

# dateはカレンダー計算をサポートしている
birthday = date(1974, 4, 15)
age = now - birthday
print(age.days) # <-- 16969
