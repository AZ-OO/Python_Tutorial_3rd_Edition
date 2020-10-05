"""
10.11 品質管理
"""

# doctestmジュールは、モジュールをスキャンし、docstringに埋め込まれた
# テストを検証するツールを提供する

def average(values):
    """
     数値のリストから算術平均を計算
    """
    print(average([20, 30, 70]))
    return sum(values) / len(values)

import doctest
doctest.testmod() # 埋め込まれたテストを自動検証する

# unittstモジュールはoctestモジュールほど楽ではないが、より包括的な一連のテストを別ファイルに持っておくことができる
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]),40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()
