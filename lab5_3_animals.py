class Cat:

    species = "Felidae"

    def __init__(self, name, collar_color):
        self.name = name
        self.collar_color = collar_color

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
        

    

if __name__ == '__main__':
    cat_one = Cat("Tom", "blue")
    cat_two = Cat("Jerry", "gray")

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