import random
from enum import Enum
from collections import Counter


class Taste(Enum):
    SWEET = 1
    SOUR = 2
    NEUTRAL = 3


class Topping(Enum):
    HONEY = 1
    LEMON = 2
    YOGURT = 3

    @property
    def Topping.taste(self):
        if self == Topping.HONEY:
            return Taste.SWEET
        elif self == Topping.LEMON:
            return Taste.SOUR
        elif self == Topping.YOGURT:
            return Taste.NEUTRAL


class Fruit:
    def __init__(self, name, size, color, taste):
        self.name = name
        self.size = size
        self.color = color
        self.taste = taste

    def __del__(self):
        print(f"{self.name} deleted")

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_taste(self):
        return self.taste

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return (
            f"Ім'я: {self.name}, розмір: {self.size}, "
            f"колір: {self.color}, смак: {self.taste.name}"
        )


class FruitSalad:
    def __init__(self, fruits=None, toppings="салат ще не заправлений"):
        if fruits is None:
            self.fruits = []
        else:
            self.fruits = fruits
        self.toppings = toppings

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def get_fruits(self):
        return self.fruits

    def get_toppings(self):
        return self.toppings

    def set_toppings(self, toppings):
        self.toppings = toppings

    def __del__(self):
        print("Фруктовий салат видалено")

    def __str__(self):
    topping_info = (
        self.toppings.name
        if isinstance(self.toppings, Topping)
        else self.toppings
    )
    lines = [f"Топінг: {topping_info}"]
    lines.extend(str(fruit) for fruit in self.fruits)
    return "\n".join(lines)
    def choose_topping(self):
    tastes = Counter(fruit.get_taste() for fruit in self.fruits)
    sweet = tastes[Taste.SWEET]
    sour = tastes[Taste.SOUR]
    neutral = tastes[Taste.NEUTRAL]

    if sweet > neutral and sweet > sour:
        self.toppings = Topping.LEMON
    elif sour > neutral and sour > sweet:
        self.toppings = Topping.HONEY
    else:
        self.toppings = Topping.YOGURT

    def mix(self):
        random.shuffle(self.fruits)


if __name__ == "__main__":
    fruit1 = Fruit("банан", "великий", "жовтий", Taste.SWEET)
    fruit2 = Fruit("персик", "середній", "рожевий", Taste.SOUR)
    fruit3 = Fruit("груша", "малий", "зелений", Taste.SWEET)
    fruit4 = Fruit("яблуко", "середній", "червоний", Taste.NEUTRAL)

    fruit1.set_name("стиглий банан")

    salad = FruitSalad()
    salad.add_fruit(fruit1)
    salad.add_fruit(fruit2)
    salad.add_fruit(fruit3)
    salad.add_fruit(fruit4)

    for fruit in salad.get_fruits():
        print(fruit.get_color())

    print("Салат до заправки та перемішування:")
    print(salad)

    salad.choose_topping()
    salad.mix()

    print("Салат після вибору топінгу та перемішування:")
    print(salad)
