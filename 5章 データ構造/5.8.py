"""
5.8 シーケンスの比較、その他の型の比較
"""

print((1, 2, 3) < (1, 2, 3))             # False
print([1, 2, 3] < [1, 2, 3])             # False
print('ABC' < 'C' < 'Python' < 'Python') # False
print((1, 2, 3, 4) < (1, 2, 4))          # True
print((1, 2) < (1, 2, -1))               # True
print((1, 2, 3) == (1.0, 2.0, 3.0))      # True
