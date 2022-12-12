class DataObject:

    def __init__(self, data) -> None:
        self.data = data
    

class Deque:

    deque = []
        
    @classmethod
    def append_left(cls, object: DataObject):
        if not isinstance(object, DataObject):
            raise NotImplementedError
        if len(cls.deque) < 5:
            cls.deque.insert(0, object)
        
    @classmethod
    def append_right(cls, object: DataObject):
        if not isinstance(object, DataObject):
            raise NotImplementedError
        if len(cls.deque) < 5:
            cls.deque.append(object)

    @classmethod
    def pop_left(cls):
        return cls.deque.pop(0)

    @classmethod
    def pop_right(cls):
        return cls.deque.pop()


a = DataObject("1")
b = DataObject("2")
c = DataObject("3")
d = DataObject("4")
e = DataObject("5")
f = DataObject("6")
a_a = Deque()
a_a.append_left(a)
a_a.append_left(b)
a_a.append_left(c)
a_a.append_left(d)
a_a.append_left(e)
a_a.append_left(f)
for i in a_a.deque:
    print(i.data)
