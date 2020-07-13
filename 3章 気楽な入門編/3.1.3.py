"""
3.1.3 リスト
角カッコの中にカンマ区切りの値(アイテム)をいれていくだけ
"""

squares = [1,4,9,16,25]
print(squares)

print(squares[0]) # インデクシングはアイテムを返す
print(squares[-1]) # インデクシングはアイテムを返す

 # スライシングは常に、要求された要素を含んだ新たなリストを返す
 # 基のリストのシャローコピーを新しく作って返す
print(squares[-3:]) # スライシングは新たなリストを作って返す

# リストは、連結をサポートしているns
# squares2 = squares + [36,49,64,81,100]
print(squares + [36,49,64,81,100])

# 文字列は変更不能体(immutable)だが、リストは変更可能体(mutable)である
# すなわち、内容を入れ替えることができる
cubes = [1,8,27,65,125] # どこかおかしい
# 4 ** 3 # 4の3乗は64だ。65じゃない！
print(4 ** 3)
cubes[3] = 64 # 間違った値を入れ替える
print(cubes)

# appens()メソッドを使うことでリストの末尾にアイテムを追加することができる
cubes.append(216) # 6の3乗を追加
cubes.append(7 ** 3) # 7の3乗を追加
print(cubes)

# スライシングへの代入も可能
# これにより、ながｓを変える事も、リストの内容を全てクリアすることもできる
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# いくつかの値を置換
letters[2:5] = ['C', 'D', 'E']
print(letters)
# 置換した内容を削除
letters[2:5] = []
print(letters)
# リストをクリア。空リストで全部の要素を置換する
letters[:] = []
print(letters)

# ビルトイン関数len()はリストにも使える
letters = ['a', 'b', 'c', 'd']
print(len(letters))

# リストは入れ子にもできる
# リストを要素とするリストが生成できる
a = ['a', 'b', 'c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1])
