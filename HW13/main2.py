class MySquareIterator:
    
    def __init__(self, lst: list):
        self.lst = lst
        self.index = 0

    def __next__(self):
        try:
            i = self.lst[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return i ** 2

    def __iter__(self):
        return self


lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for el in itr:
	 print(el, end=" ")
