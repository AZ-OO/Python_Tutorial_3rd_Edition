"""
7.2.1 ファイルオブジェクトのメソッド
"""
f = open('workfile', 'r')
print(f.read())
print(f.read())
f.close()

# f.readline()はファイルから1行読む
# f.readline()が空の文字列を返せば、ファイルの末尾に達したという事
f2 = open('workfile2', 'r')
print(f2.readline())
print(f2.readline())

# 行単位の読み込みには、ファイルオブジェクトにループをかける方法がある
# これはメモリ効率に優れ、高速な↑、コードが簡単になる
f2 = open('workfile2', 'r')
for line in f2:
    print(line,end = '')
f2.close()
#f.write(文字列)は、文字列の内容をファイルに書き込み、書き込まれたキャラクタの数を返す
f3 = open('workfile2', 'a')
print(f3.write('This is a test\n'))

# 文字列でないモノを書き込む時は、文字列に変換しておく必要がある
value = ('the answer', 42)
s = str(value)
print(f3.write(s))
f3.close()

f4 = open('workfile3', 'rb+')
print(f4.write(b'0123456789abcdef'))
print(f4.seek(5)) # ファイルの6バイト目に行く
print(f4.read(1))
print(f4.seek(-3, 2)) # ファイル末尾から3バイト前に行く
print(f4.read(1))
f4.close()

# ファイルオブジェクトを扱うときはキーワードwithを使うというのがよい習慣だ
# その利点は、一連の操作から抜ける時にファイルが正しく閉じられる
# これは、途中え例外が送出されたとしても処理される
# 同等の操作になるtry-finallyブロックよりずっと短い
with open('workfile', 'r') as f:
    read_data = f.read()
print(read_data)
f.closed
