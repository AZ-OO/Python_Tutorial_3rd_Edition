"""
10.6 数学
"""

# mathモジュールを使うと、浮動小数点数数学用の下層のCライブラリ関数にアクセスできる

import math
print(math.cos(math.pi / 4)) # <-- 0.7071067811865476
print(math.log(1024, 2))     # <-- 10.0

# randomモジュールは無作為抽出のツールを提供する
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10)) # 重複なしの抽出      <-- [40, 83, 75, 95, 55, 66, 8, 84, 57, 96]
print(random.random())               # ランダムな浮動小数点 <-- 0.11638404874734021
print(random.randrange(6))           # range(6)からランダムに選んだ整数

# statisticsモジュールは数値データの基本統計量(平均、中央値、分解など)を求めるもの
import statistics
data = [2.75 ,1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean((data))) # 平均   <-- 1.6071428571428572
print(statistics.median(data)) # 中央値 <-- 1.25
print(statistics.variance(data)) # 分散 <-- 1.3720238095238095
