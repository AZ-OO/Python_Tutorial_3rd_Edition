"""
6.1 さらにモジュールについて
"""

# ファイルに定義を仕込んでスクリプトや対話セッションをもつ。このファイルをモジュールといいう
# モジュールとは、Pythonの定義や文がはいったファイルである
import fibo # モジュールをインポート
print(fibo.fib(1000))

print(fibo.fib2(100))

print(fibo.__name__)

fib = fibo.fib # 関数をローカル変数に代入
print(fib(500))

from fibo import fib, fib2
print(fib(300))

from fibo import *
print(fib(400))
