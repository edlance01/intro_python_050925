s = "3"             # string
i_1 = 12            # integer
i_2 = 4             # integer
i_3 = 3             # integer
f = 16.12           # float
pi = 3.1415926535   # float
b_1 = True          # boolean
b_2 = False         # boolean

# to check type
print(type(s)) # <class 'str'>

'''
Below, we are adding a string and an integer. 
To do this addition, we must convert the string to an integer.
This only works because the string's value is "3".
'''
print(int(s) + i_1) # 15

'''
The example below is another way to add a string and an integer.
This time, we converted the integer to a string.
'''
print(s + str(i_1)) # 312

'''
Convert a string to an int
'''
print(int(s)) # 3

'''
When we add an integer and a float, the integer gets promted to a float.
That's why the result is a float.
'''
print(i_1 + f) # 28.12

'''
When we add an integer and a boolean, the boolean gets assigned an integer value.
True = 1 and False = 0
'''
print(i_2 + b_1) # 5

'''
When we add a float and a boolean, the boolean still gets assigned the same integer value.
Then, the integer gets promoted to a float, and the result is a float.
'''
print(pi + b_2) # 3.1415926535

'''
The example below is using regular division.
This will be the exact result of the division.
'''
print(9/2) # 4.5

'''
This example is using floor division.
The exact result is rounded down to the nearest whole number.
'''
print(9//2) # 4


# boolean - specs say any non zero integer is True...but be careful (see notes below)
bool_shoot = 2
if bool_shoot == True:  # True in Python is 1 so this fails
    print("It's True")
else:
    print("It's False")  # bool_shoot w/value prints "It's False"

print(
    bool(bool_shoot)
)  # This prints True.  bool function converts a number to a boolean.

my_b = True
print(f"True + 3: {my_b + 3}")

"""
Any non-zero integer in Python is considered "truthy" – meaning when evaluated in a Boolean context (like the condition of an if statement or when passed to bool()), it behaves like True.
However, the Boolean value True is actually represented internally as the integer 1. This is why the comparison bool_shoot == True (which is 2 == 1) evaluates to False.
"""