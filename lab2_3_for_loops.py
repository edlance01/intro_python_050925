"""
Create a for loop that iterates over a range of positive numbers of your choosing
"""
for i in range(101,105):
    print(i)


"""
Using an if-else block, print if the number is even or odd
Hint: You should use the modulus operator here
"""
print("\n Print Even or Odd")
for x in range(10,20):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

"""
Challenge: Create a nested for loop that prints out a multiplication table 
"""
print("\n*** Mulitplication Table ***")
for a in range(1,10):
    for b in range(1,10):
        print(a*b, end=" ")
    print()

# print a final line
print("-" * 50)