"""
9.7 残り物あれこれ
"""

class Employee:
    pass

john = Employee() # 空の従業員レコードを作成


# レコードのフィールドを埋めていく
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.name)
print(john.dept)
print(john.salary)
