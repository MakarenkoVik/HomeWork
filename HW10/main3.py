class Counter:

    def __init__(self, start: int = 0, stop: int = None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.stop == None or self.start < self.stop:
            self.start += 1
        else:
            print("Maximal value is reached.")
        return self.start

    def get(self):
        print(self.start)


c = Counter(start=44)
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
