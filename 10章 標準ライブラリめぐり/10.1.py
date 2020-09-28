"""
10.1 OSインターフェース
"""

"""
# OSモジュールはオペレーティング・システムとやり取りする関数を何ダースか適用する
import os
print(os.getcwd())                                                                         # 今いるディレクトリを返す
os.chdir('/Users/Osamu/PycharmProjects/Python_Tutorial_3rd_Edition/9章 クラス')             # カレントディレクトリ変更
os.chdir('/Users/Osamu/PycharmProjects/Python_Tutorial_3rd_Edition/10章 標準ライブラリめぐり') # カレントディレクトリ変更
os.system('mkdir test')                                                                    # システム側のシェルでmkdirコマンドを実行

# OSなどの大きなモジュールを使うときは、ビルトイン関数のdir()とhelp()っを相談相手にするとよい
import os
dir(os) # モジュールの関数が全て入ったリストをかえしてくる
help(os) # モジュールのdocstringかあｒ生成された詳細なマニュアルを返してくる
"""

# 日々のファイルやディレクトリの管理には、shutilモジュールによる使いやすい高水準インターフェースがよい
import shutil
shutil.copyfile('data.db', 'archivedb') # ファイルを名前を指定してコピー
# ファイルを指定のディレクトリに移動
shutil.move('/Users/Osamu/PycharmProjects/Python_Tutorial_3rd_Edition/10章 標準ライブラリめぐり/data.db',
            '/Users/Osamu/PycharmProjects/Python_Tutorial_3rd_Edition/10章 標準ライブラリめぐり/test')
