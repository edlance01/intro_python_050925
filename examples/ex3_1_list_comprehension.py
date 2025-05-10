divider = "-" * 50

# create a list with for loop
squares = []  # empty list
for i in range(5):
    squares.append(i**2)
print(squares)

print(divider)

# create the same list using list comprehension
# [expression for item in iterable]
squares_comprehension = [x**2 for x in range(5)]
print(squares_comprehension)

print(divider)

# optional if statement with list comprehension (e.g. for filtering)

# first the traditional way
even_numbers = []
for y in range(10):
    if y % 2 == 0:
        even_numbers.append(y)
print(even_numbers)

print(divider)

# now with list comprehension
even_nums_comp = [y for y in range(10) if y % 2 == 0]
print(even_nums_comp)

print(divider)

# note you can manipulate  / transform elements too
doubled_odds = [z * 2 for z in range(1,6) if z % 2 != 0]
print(doubled_odds)