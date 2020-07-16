"""
5.7 条件についての補足
"""

# 比較演算子in及びnot inはシーケンスに値が存在するか(および存在しないか)をチェックする
# 演算子is及びis notは、2つのオブジェクトを比較して完全に同一であるかを調べる


srting1, string2, string3 = '','Trondheim','Hammer Dance'
non_null = string2 or string2 or string3
print(non_null)
