def recursive_id(num=1):
    global students
    if num not in students:
        return num
    else:
        return recursive_id(num + 1)


students = {3: "Sam", 7: "John"}
studentList = ["Carlos", "Matt", "Luke", "Jordan"]

# create a recursive function that generates the next available unique ID
unique_id = 1;

for student in studentList:
    unique_id = recursive_id()
    students[unique_id] = student

# print the updated student list
print("-" * 50)
for id, name in students.items():
    print(f"Id:{id} Name:{name}")

# optional - sort
"""
students.items() returns a view object that displays a list of a dictionary's key-value tuple pairs (e.g., [(3, 'Sam'), (7, 'John'), ...]).
sorted(students.items()): When you pass this list of tuples to the sorted() function, it sorts these tuples by default based on the first element of each tuple, which in this case are the keys (your 'Id' values).
"""
sorted_students_by_id = sorted(students.items())

print("-" * 50)
print("Sorted by Id")
for id, name in sorted_students_by_id:
    print(f"Id:{id} Name:{name}")
