import time
from main1 import Auto


class Truck(Auto):

    max_load = 500

    def drive(self):
        print("Attention!")
        super().drive()

    def load(self):
        time.sleep(1)
        print("Load.")
        time.sleep(1)


class Sedan(Auto):

    max_speed = 120

    def drive(self):
        super().drive()
        print(f"Max speed of sedan {self.brand} {self.mark} is {self.max_speed}.")


bmw = Truck("BMW", 3, "M4")
bmw.drive()
bmw.load()
print(f"Max load {bmw.max_load}.")
honda = Truck("Honda", 11, "Accord")
honda.drive()
honda.load()
print(f"Max load {honda.max_load}.")

ford = Sedan("Ford", 5, "Mondeo")
ford.drive()
kia = Sedan("Kia", 5, "Rio")
kia.drive()
