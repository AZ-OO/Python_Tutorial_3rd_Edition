"""
5.1.1 リストをスタックとして使う
"""

# スタックでは最後に追加された要素が最初に取得される(後入れ先出し (last-in, first-out)
# スタックのトップにアイテムを積むにはappens()を使う。
# スタックのトップからアイテムを取得するには、pop()を使う。

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

