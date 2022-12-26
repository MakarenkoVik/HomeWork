from dataclasses import dataclass


@dataclass
class InvalidIntDivision(Exception):
    i: int
    name: str = "InvalidIntDivision"

    def __str__(self) -> str:
        return f"{self.name} # {self.i}"


@dataclass
class InvalidIntNumberCount(Exception):
    i: int
    name: str = "InvalidIntNumberCount"

    def __str__(self) -> str:
        return f"{self.name} # {self.i}"


@dataclass
class InvalidFloat(Exception):
    i: float
    name: str = "InvalidFloat"

    def __str__(self) -> str:
        return f"{self.name} # {self.i}"


@dataclass
class InvalidTextLength(Exception):
    i: str
    name: str = "InvalidTextLength"

    def __str__(self) -> str:
        return f"{self.name} # {self.i}"


@dataclass
class DuplicatesInText(Exception):
    i: str
    name: str = "DuplicatesInText"

    def __str__(self) -> str:
        return f"{self.name} # {self.i}"


class Queue:

    def __init__(self):
        self.queue = []
        self.errors = []

    def add(self, *args):
        for i in args:
            if isinstance(i, int):
                if i % 8:
                    self.errors.append(InvalidIntDivision(i))
                if len(str(i)) > 4:
                    self.errors.append(InvalidIntNumberCount(i))
                if i % 8 == 0 and len(str(i)) <= 4:
                    self.queue.append(i)
            elif isinstance(i, float):
                ii = str(i).split(".")
                if len(ii[1]) > 2:
                    self.errors.append(InvalidFloat(i))
                else:
                    self.queue.append(i)
            elif isinstance(i, str):
                symbols = []
                if len(i) > 4:
                    self.errors.append(InvalidTextLength(i))
                for symbol in i:
                    if symbol not in symbols:
                        symbols.append(symbol)
                    else:
                        self.errors.append(DuplicatesInText(i))
                        break
                if len(i) <= 4 and symbols:
                    self.queue.append(i)
        for error in self.errors:
            print(error)
        self.errors = []


a = Queue()
a.add(5, 96592.545, 2, 8, "qqqiii", "qwertyuii", 54524.4, "dtj", "dgi")
print(a.queue)
