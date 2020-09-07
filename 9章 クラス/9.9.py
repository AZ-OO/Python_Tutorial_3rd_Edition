"""9.9 反復子 (iterator)""""""for element in [1, 2, 3]:    print(element)for element in (1, 2, 3):    print(element)for key in {'One':1, 'Two':2}:    print(key)for char in '123':    print(char)for line in open('myfile.txt'):    print(line, end='')s = 'abc'it = iter(s)# <iterator object at 0x00A1D850>print(next(it))print(next(it))print(next(it))print(next(it))# Tracrback (most recent call last):    File '<stdin>', line 1, in?        next(it)StopIterator"""class Reverse:    # シーケンスを逆順にループする反復子    def __init__(self, data):        self.data = data        self.index = len(data)    def __iter__(self):        return self    def __next__(self):        if self.index == 0:            raise StopIteration        self.index = self.index - 1        return self.data[self.index]rev = Reverse('spam')iter(rev)for char in rev:    print(char)