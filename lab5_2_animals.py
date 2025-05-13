class Cat:

    species = "Felidae"

    def __init__(self, name, collar_color):
        self.name = name
        self.collar_color = collar_color

if __name__ == '__main__':
    cat_one = Cat("Tom", "blue")
    cat_two = Cat("Jerry", "gray")

    print(cat_one.name)
    print(cat_one.collar_color)
    print(cat_one.species)
    
    print(cat_two.name)
    print(cat_two.collar_color)
    print(cat_two.species)
    