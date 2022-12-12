class Dish:

    def __init__(self, amount: int, name_dish: str, weight: float, price: float):
        self.amount = amount
        self.name = name_dish
        self.weight = weight
        self.price = price
    

class Order:

    def __init__(self):
        self.dishes = []
        
    def add_dish(self, dish: Dish):
        if dish.amount > 1:
            dish.amount -= 1
        else:
            print("Данного блюда нет в наличии, извините.")
        self.dishes.append(dish)

    def order_cost(self):
        self.price = 0
        for i in self.dishes:
            self.price += i.price
        return f"{self.price:.2f}"

    def prepayment(self, money: float):
        self.money = money
        return money

    def balance(self):
        return self.price - self.money


dish_1 = Dish(15, "chicken soup", 0.2, 5.0)
dish_2 = Dish(30, "potatoes with mushrooms", 0.3, 7.30)
dish_3 = Dish(20, "salad", 0.15, 4.15)

order = Order()
order.add_dish(dish_1)
order.add_dish(dish_2)
order.add_dish(dish_3)
order.add_dish(dish_1)
print(order.order_cost())
print(order.prepayment(10))
print(order.balance())
