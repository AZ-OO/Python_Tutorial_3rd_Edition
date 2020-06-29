"""
4.4 break文とontinue文、ループにおけるelse節
"""

# break文は、forまたはwhileのループを抜けるモノ
# ループ文にはelse節が加えられる
# else節はリストを使い果たしたり(for)、条件式がfalesになること(while)によって
# ループが終了したバアアイに実行され、
# break文で終了した場合には実行されない

# 素数検索ループ
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # ループの約数を見つけられなかった場合
        print(n, 'is a prime number')

# continue文
for num in range(2,10):
    if num % 2 == 0:
        print('Foound as even number', num)
        continue
    print('Found a number', num)
