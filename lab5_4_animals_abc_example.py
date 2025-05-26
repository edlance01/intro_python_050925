from abc import ABC, abstractmethod

class Cat(ABC):

        species = "Felidae"

        def __init__(self, name, collar_color):
            self.__name = name
            self.__collar_color = collar_color

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
            print("All cats eat the same")

        def scratch_furniture(self, mood):
            amount = 0.0
            if mood == "happy":
                amount = 1.00
            elif mood == "grumpy":
                amount = 15.00
            else:
                amount = 5.00

            return amount

        @abstractmethod
        def watch_tv(self):
            pass


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

    def watch_tv(self):
        print("BengalCat has to watch TV from outside the house.")


class HouseCat(Cat):

    def watch_tv(self):
        print("HouseCat can watch tv from inside the house")


if __name__ == "__main__":
    cat_one = HouseCat("Tom", "blue")
    cat_two = HouseCat("Jerry", "gray")
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
 
    print("\n------------------------------------------")
    cats = [cat_one, cat_two, bengal_one]
    for cat in cats:
        cat.watch_tv()
