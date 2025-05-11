"""
Encapsulating State and Behavior (Closures):

When a function returns an inner function, that inner function can "remember" the variables from the outer function's scope, even after the outer function has finished executing. This is called a closure.
"""
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print(my_counter())
print(my_counter()) # 2
print(my_counter()) # 3 ...as you can see it has access to and remembers count

#new copy
another_counter = counter()
print(another_counter())