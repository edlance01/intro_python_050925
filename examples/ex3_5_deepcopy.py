import copy  # deepcopy comes from the copy module

list1 = [1, 2, [3, 4]]
list3 = copy.deepcopy(list1)

print(f"Original list (list1): {list1}")
print(f"Deep copy (list3): {list3}")

# Modifying an element in the outer list of the deep copy
list3[0] = 100
print(f"\nAfter modifying outer element of deep copy:")
print(f"Original list (list1): {list1}")
print(f"Deep copy (list3): {list3}")

# Modifying an element in the inner list of the deep copy
list3[2][0] = 300
print(f"\nAfter modifying inner element of deep copy:")
print(f"Original list (list1): {list1}")
print(f"Deep copy (list3): {list3}")
