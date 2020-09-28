"""
10.3 コマンドライン引数
"""

# ユーティレティスクリプトではコマンドライン引数を処理する場合が多い。
# 引数はsysモジュールのargv属性にリストとして格納されている
# ターミナルで[python 10.3.py one twh three]を実行
import sys
print(sys.argv) # <--['10.3.py', 'one', 'two', 'three']
