import os
print(f"Current working directory: {os.getcwd()}")

from animal_util import choose_random_meal as meal

class Cat:
    species = "Felidae"

    def __init__(self, name, collar_color):
        self.__name = name
        self.__collar_color = collar_color
        # _Cat__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self.__name = value

    @property
    def collar_color(self):
        return self.__collar_color

    @collar_color.setter
    def collar_color(self, value):
        if not isinstance(value, str):
            raise TypeError("Collar color must be a string")
        self.__collar_color = value

    def eat(self):
       # print("All cats eat the same")

       print(f"Dinner this evening is: {meal()}")


    def scratch_furniture(self, mood):
        amount = 0.0
        if mood == "happy":
            amount = 1.00
        elif mood == "grumpy":
            amount = 15.00
        else:
            amount = 5.00

        return amount


class BengalCat(Cat):
    def __init__(self, name, collar_color, stripe_pattern):
        super().__init__(name, collar_color)
        self.__stripe_pattern = stripe_pattern

    @property
    def stripe_pattern(self):
        return self.__stripe_pattern

    @stripe_pattern.setter
    def stripe_pattern(self, value):
        if not isinstance(value, str):
            raise TypeError("Stripe pattern must be a string")
        self.__stripe_pattern = value

    def scratch_furniture(self, mood):  # slight change in behavior
        amount = 0.0
        if mood == "hungry":
            amount = 500.00
        else:
            amount = 100.00

        return amount

        # another option to think about
        # amount = super().scratch_furniture(mood)
        # if mood == "playful":
        #     amount *= 2
        # return amount

    def climb_tree(self):  # New behavior
        print(f"{self.name} is climbing a tree with amazing agility!")


if __name__ == "__main__":
    cat_one = Cat("Tom", "blue")
    cat_two = Cat("Jerry", "gray")
    bengal_one = BengalCat("Raja", "red", "rosette")

    print(cat_one.name)
    print(cat_one.collar_color)
    print(cat_one.species)
    cat_one.eat()
    print(cat_one.scratch_furniture("grumpy"))

    print(cat_two.name)
    print(cat_two.collar_color)
    print(cat_two.species)
    cat_two.eat()
    print(cat_two.scratch_furniture("happy"))

    print(bengal_one.name)
    print(bengal_one.collar_color)
    print(bengal_one.species)
    bengal_one.eat()
    print(bengal_one.scratch_furniture("hungry"))
    bengal_one.climb_tree()  # Call the new method
