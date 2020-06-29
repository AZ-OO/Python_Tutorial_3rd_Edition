"""
3.1.2 文字列
"""
# シングルクォート
single = 'spam eggs'
print(single)

# シングルクォートは\でエスケープするか…
# nのあとにシングルクォートが表示される
esc = 'dosen\'t'
print(esc)

# ダブルクォートと使う
des = "dosen't2"
print(des)

# 文字列にダブルクォートを含む
msg1 = '"Yes", he said'
print(msg1)

# 文字列に\を含む
msg2 = "\"Yes,\" he said."
print(msg2)

msg3 = '"Isn\'t," she said.'
print(msg3)

msg4 = '"Isn\'t," she said.2'
print(msg4)

print('"Isn\'t," she said.3')

# \nは改行の意味
s = 'First Line. \nSecond Line.'
print(s)

# 「\」を前置した文字が特殊文字に解釈されるのが嫌なときは、raw過文字列を使えう
# 最初の引用符の前にrをおく

print('C;\some\name1') # \nは改行なので
print(r'C;\some\name2') # 引用符の前のrに注目

# 文字列リテラルを複数行にわたり書くことも可能
# ひとつの方法はトリプルクォート("""..."""または'''...''')
# 行末文字は自動的に文字列に含有される
# これを避けたいときは行末に\を置く


# 最初の改行が含まれないことに注目
print("""\
Usage:thingy[OPTIONS]
-h                   Display this usage message
-H hostname          Hostname to comment to
""")

# 文字列は+演算子で連結できるし、　*演算子で繰り返すこともできる
# unを3回繰り返して、最後にiumを付ける
msg5 = 3 * 'un' + 'ium'
print(msg5)

# 列挙された文字列リテラル(引用符で囲まれたものたち)は自動的に連結される
msg6 = 'Py' 'thon'
print(msg6)

# 自動的に連結されるる機能は、長い文字列を分割したいときに便利
text = ('カッコの中に長い長い長い文字列を'
        '入れておいてつなげてやろう')
print(text)

#  ただし、これはリテラル同士でのみ有効で、変数や式では無効
# エラーとなるのでコメントアウト
# prefix = 'Py'
# text2 =prefix 'thon' #  変数と文字列リテラルは連結できない
# print(text2)


# 変数とリテラルの連結、そして変数同士の連結には+を使う
prefix = 'Py'
text3 = prefix + 'thon3'
print(text3)

# 文字列はインデックス指定(連番による指定)ができる
# 最初のキャラクタのインデックスは0
word = 'Python'
text4 = word[0] # 位置0のキャラクタ
print(text4)
text5 = word[5]
print(text5)

# インデックスには負の数も使える
# これは右から数えることを示す
# -0と0は同じことなので、負のインデックスは-1から始まる
text6 = word[-1] # 最後のキャラクタ
print(text6)
text7 = word[-2] # 最後から2番目のキャラクタ
print(text7)
text8 = word[-6]
print(text8)

# インデックスの他にスライシング(切取)もサポートされている
# スライシングは部分文字列(サブスオリング)が取得できる
text9 = word[0:2] # 位置0から(0を含み)2まで(2を含まない)の文字
print(text9)
text10 = word[2:5] # 位置2から(2を含み)5まで(5を含まない)の文字
print(text10)

# スライシングには便利なデフォルト値がある
# 愛1文字の省略時のデフォルトが0、
# 第2文字の省略時のデフォルトが文字列のサイズとなっている
text11 = word[:2] # 最初の文字から位置2まで(2を含まない)の文字
print(text11)
text12 = word[4:] # 位置4から(4を含む)最後までの文字
print(text12)
text13 = word[-2:] # 位置-2(-2を含む)から最後までの文字
print(text13)

# 大きすぎるインデックスを指定するとエラーとなる
# エラーとなるため、コメントアウト
# text14 = word[42]
# print(text14)

# スライシングは範囲外のインデックスをしていいても、いい具合に処理してくれる
text15 = word[4:42]
print(text15)
text16 = word[42:]
print(text16)

# Pythonの文字列は改変できない -- 変更不能体(Immutable)である
# このため、文字列のインでっ靴位置に代入を行うとエラーとなる
# エラーとなるため、コメントアウト
# word[0] = 'j'
# print(word)
# word[2:] = 'Py'
# print(word)

# 異なる文字列が必要な時は新しい文字列を生成する必要がある
text17 = 'j' + word[1:]
print(text17)
text18 = word[:2] + 'Py'
print(text18)

# ビルトイン関数len()は文字列の長さを返す
s = 'abcdefghijklmnopqrstuvwxyz'
print('変数sは ' + str(len(s)) + ' 文字')


