class Auto:

    color = "black"
    weight = 2

    def __init__(self, brand: str, age: float, mark: str):
        self.brand = brand
        self.age = age
        self.mark = mark

    def drive(self):
        print(f"Car {self.brand} {self.mark} drives.")

    def stop(self):
        print(f"Car {self.brand} {self.mark} stops.")
    
    def use(self):
        self.age += 1
        return self.age


audi = Auto("Audi", 5, "Q7")
audi.drive()
audi.stop()
print(audi.use())
