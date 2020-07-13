"""
if文
"""

x = int(input('整数を入力してください'))
if x < 0:
    x = 0
    print('負数はゼロとする')
elif x == 0:
    print('ゼロ')
elif x == 1:
    print('ひとつ')
else:
    print('もっと')

