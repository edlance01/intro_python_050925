

def hello_print():
    print("Hello functions!")

def hello_return():
    return "Hello functions!"

def hello_generator():
    for character in "Hello functions!":
        yield character

if __name__ == '__main__':
    hello_print()
    print(hello_return())

    for ret in hello_generator():
        print(ret, end= " ")
