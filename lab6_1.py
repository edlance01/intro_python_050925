import random
import string
import math

div = "\n" + "-" * 50

print(div, "\nExample of using dir with math:")
print(dir(math))

print(div, "\nExample of randrange:")
print(random.randrange(0, 105, 5))

print(div, "\nExample of 50 random ascii characters:")
for i in range(0, 50):
    print(random.choice(string.ascii_letters), end = "")

print(div, "\nCreating and running circumference function:")
def circumference(r):
    return 2 * math.pi * r

cir = circumference(5)
print(f"The circumference of your circle is: {cir:.2f}")

print("\nFloating sum function with a list:", div)
lis = [2, 4, 6, 8 , 10]
print(math.fsum(lis))

