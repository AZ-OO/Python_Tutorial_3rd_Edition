"""
4.7.7 関数注釈(関数アノテーション)
"""
#

def my_func(ham: str, eggs: str = 'eggs2') -> str:
    print('Annotations:', my_func.__annotations__)
    print('Arguments:', ham, eggs)
    return ham + ' and ' + eggs

print(my_func('spam'))
