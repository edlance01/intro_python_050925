pdiv = lambda: print("-" * 50)

# lambda arguments: expression

# simple lambda to add two numbers
add = lambda x, y: x+y
print(add(5,7))

# lambda that squares a number
square = lambda num: num**2
print(square(5))

# lambda with no args, always returns "Hello"
greet = lambda: "Hello"
print(greet())

"""
Lambdas become particularly powerful when you use them with higher-order functions i.e.
functions that take other functions as arguments or return functions.
map() and filter() are built in higher-order functions in python.
"""

# map - applies a fiven function to each item of an iterable and returns an iterator of the results
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
pdiv()
print(squared_numbers)

# filter - creates a new iterable with elements from the original iterable which a given
# function returns true
numbers2 = [11,12,13,14,15,16]
even_numbers = list(filter(lambda x: x %2 == 0, numbers2))
pdiv()
print(even_numbers)

"""
sorted() - sorts the items of an iterable.
You can provide a key argument, which is a function to be called on each list element
prior to making comparisons.  Lambdas work great for this.
"""
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "C"},
]

sorted_by_grade = sorted(students, key=lambda student: student["grade"])
pdiv()
print(sorted_by_grade)
# Output: [{'name': 'Bob', 'grade': 'A'}, {'name': 'Alice', 'grade': 'B'}, {'name': 'Charlie', 'grade': 'C'}]

sorted_by_name_length = sorted(students, key=lambda student: len(student["name"]))
pdiv()
print(sorted_by_name_length)
# Output: [{'name': 'Bob', 'grade': 'A'}, {'name': 'Alice', 'grade': 'B'}, {'name': 'Charlie', 'grade': 'C'}]
