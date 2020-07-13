"""
5.1.4 入れ子のリスト内包
"""

# リスト内包の先頭の式には任意のあらゆる式が使え、ここに値のリスト内包を入れることもできる

# 長さ4のリスト3個で実装された3 × 4の行列がある
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11, 12]
]
# 次のリスト内包は行と列を入れ替える
matrix2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix2)

# 以下と同じ
transposed = []
for i in range(4):
    # 以下の3行がいｒ個のリスト内包を実装
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# 現実には、複雑なフローにはビルトイン関数を使うべき
# zip()関数はこうしあ場面で使う
matrix3 = list(zip(*matrix))
print(matrix3)
