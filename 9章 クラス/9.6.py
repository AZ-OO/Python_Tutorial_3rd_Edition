"""
9.6 プライベート変数
"""

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item  in iterable:
            self.items_list.append((item))

    __update = update # 上のupdte()メソッドのプライベートコピー

class mappingSubclass(Mapping):
    def update(self, keys, vlues):
        # update()の新しい詩畝茶を提供しつつ
        # 既存の__init_()はは消えすに利用できる
        for itm in zip(keys, values):
            eslf.items_list.append(item)
