div = "-" * 50 + "\n"

def sum_is_even(num1, num2=0):
    is_even = False
    if (num1 + num2) % 2 == 0:
        is_even = True
    
    return is_even

def arg_ex(*args):
    # for arg in args:
    #     print(arg)
    [print(arg) for arg in args]


def kwargs_ex(**kwargs):
    # for key, value in kwargs.items():
    #     print(f"{key} = {value}")

    [print(f"key:{key} = value:{value}") for key, value in kwargs.items()]


if __name__ == '__main__':

    print(div)
    print(sum_is_even(10))
    print(sum_is_even(10,5))
    print(sum_is_even(num2 = 8, num1 = 7))

    print(div)
    arg_ex(4,1,1)

    print(div)
    kwargs_ex(a="first", b="second", c="third")
