
"""
*args is a variable number of positional arguments, passed as a tuple
"""
def function_a(*args):
    for arg in args:
        print(arg)


"""
**kwargs is a variable number of keyword arguments, passed as a dictionary
"""
def function_b(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")



if __name__ == '__main__':
    # using *args
    function_a("one", "two", "three")
    function_a(4,5,6)
    function_a() # look, no args
    print("-" * 50 + "\n")

    # using **kwargs
    function_b(a="apple", b="bannana")
    function_b()
    print("-" * 50 + "\n")