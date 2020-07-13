"""
4.7.3 任意引数のリスト
"""

# 関数を任意個数の引数でコール
# これにより、引数はタプルにまとめられる
# 可変長の引数は仮引数リストの最後に置く
def write_multiple_items(file, separator, *args):
    file.write(separatpr.join(args))

def concat(*args, sep='/'):
    return sep.join(args)
print(concat('Earth', 'mars', 'venus'))

print(concat('earth', 'mars', 'venus', sep='.'))

