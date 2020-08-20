"""
8.1 構文エラー
"""
# エラーには2つの種類がある
# 構文エラー(syntax error)と例外(exception)である
# 構文エラー
# while True print('Hello world') <-- SyntaxError: invalid synta(構文エラー : 無効な構文)

"""
8.2 例外
"""
# 10 * (1/0) <-- ZeroDivisionError: division by zero(ゼロ除算エラー : 0で割りました)

# 4 + apam * 3 <-- NameError: name 'apam' is not defined(名前エラー : 名前「spam」は定義されていない)

# '2' + 2 <-- TypeError: can only concatenate str (not "int") to str(型エラー : 整数オブジェクトは文字列オブジェクトに暗黙変換できない)

"""
8.3 例外の処理
"""
'''
while True:
    try:
        x = int(input('数字を入れてください：'))
        break
    except ValueError:
        print('あらら！これは有効な数字ではありません。どうぞ、もう一度…')
    except (RuntimeError, TypeError, NameError):
        pass
'''
'''
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
except OSError as err:
    print('OS error: {0}'.format(err))
except ValueError:
    print('データが整数に変換できません。')
except:
    print('予期せぬエラー:',sys.exc_info()[0])
    raise # 例外の再送出
'''
# tty...except文には、オプションでelse節が入れられる
# 位置はすべてのexcept節より後ろでなければならない
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
