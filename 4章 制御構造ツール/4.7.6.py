"""
4.7.6 ドキュメンテーション文字列(docstring)
"""

# 1行目にはいつでも常にオブジェクトの目的の短く簡潔な要約とすべき。
# とにかく簡単に、オブジェクトの名前や型といった他でおえられることを明示するｋとはしない
# ただし、関数名がすでにその動作を説明する動詞になっている場合は例外
# さらに続きがある場合は、ドキュメンテーション文字列の2行目を空行とする
# 要約と他の記述を視覚的に分離すべきである
# 以降の行では安楽を使い、そのオブジェクトのコールのしかたや副作用などを記述すべきである
# Pythonのパーサは、複数行からなる文字列リテラルのインデントを除去しないので、
# 除去したい場合は、ドキュメントを処理するツールの方で行う必要がある

def my_function():
    """Do nothing but document it.

    No really, it dosen't do anything
    """
    pass
print(my_function.__doc__)
