"""
10.4 エラー出力のリダイレクト(行き先を変えること)とプログラムの終了
"""
# sysモジュールには、stdin、stdout、stderrといった属性もついている。
# stderrは、stdoutがリダイレクトされている際にも警告やエラーメッセージが見えるようにするのに便利

import sys
sys.stderr.write('Warning, log file not found starting a new one\n')
# 警告、ログ・ファイルがないから作りますよ

sys.exit() # 一番直接てきな方法でスクリプトを終了したいときはsys.exit()を使う
