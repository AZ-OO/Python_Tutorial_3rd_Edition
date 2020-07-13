"""
5.1.2 リストをキューとして使う
"""

# キューでは要素を入れた順に取得する(先入れ先出し First-in, First-out)

from collections import deque
queue = deque(['Eric', 'john', 'Michael'])
print(queue)
queue.append('Terry')  # テリーが来た
queue.append('Graham') # グレアムが来た
queue.popleft()        # 最初に来た者が去る
print(queue)
queue.popleft()        # 2番目に来た者が去る
print(queue)           # 北順に並んだキューの状態
