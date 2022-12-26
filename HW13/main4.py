class EvenRange:
    
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __next__(self):
        while self.stop > self.start:
            if self.start % 2:
                self.start += 1
            else:
                t = self.start
                self.start += 1
                return t
        raise Exception("Out of number")

    def __iter__(self):
        return self


er1 = EvenRange(9,13)
print(next(er1))
print(next(er1))
print(next(er1))
