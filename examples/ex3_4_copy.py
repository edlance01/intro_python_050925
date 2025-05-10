"""
When you use copy(), you're essentially creating a new object, but this new object 
contains references to the original object's contents.
For simple objects (like a list of numbers or strings), the new copy is independent
 of the original. Changes you make to the copy won't affect the original, and vice versa.
However, if your object contains other mutable objects (like a list of lists or a dictionary
containing lists), the copy() will only create new references to these inner objects.
This means that if you modify an inner object in the copy, the change will also be reflected
in the original, and vice versa.
"""

list1 = [1, 2, [3, 4]]
list2 = list1.copy()

print(f"Original list (list1): {list1}")
print(f"Shallow copy (list2): {list2}")

# Modifying an element in the outer list of the copy
list2[0] = 10
print(f"\nAfter modifying outer element of copy:")
print(f"Original list (list1): {list1}")
print(f"Shallow copy (list2): {list2}")

# Modifying an element in the inner list of the copy
list2[2][0] = 30
print(f"\nAfter modifying inner element of copy:")
print(f"Original list (list1): {list1}")
print(f"Shallow copy (list2): {list2}")

listC = []
listA = ["a","b","c"]
listB = ["x","y","z"]
listA[1] = listB
print(f"listA after assignment of B: {listA}")

listC = listA.copy()
print(f" initial listC: {listC}")

listB.append("rst")
print(f"listA after inner list (B) update:{listA}")
print(f"listC after inner list (B) update:{listC}")
