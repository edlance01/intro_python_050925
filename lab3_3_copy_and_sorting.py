import copy

divide = "-" * 50 + "\n"

famous_guitarists = [
        "Jimi Hendrix",
        "Jimmy Page",
        "Eric Clapton",
        "Eddie Van Halen",
        "B.B. King",
        "Chuck Berry",
        "Keith Richards",
        "Stevie Ray Vaughan"
]

fg_sorted = sorted(famous_guitarists)
print(f"\nfg_sorted: {fg_sorted}")
print(f"\nfamous_guitarist after sorted: {famous_guitarists}")
print(divide)

famous_guitarists.sort()
print(f"\nfamous_guitarist after sort(): {famous_guitarists}")
print(divide)

nums = [8,1,9,2,7,4,5,6,3]
nums_sorted = sorted(nums)
print(f"\nnums_sorted: {nums_sorted}")
print(f"\nnums after nums_sorted: {nums}")
print(divide)

nums.sort()
print(f"\nnums_sort: {nums}")
print(f"\nnums after nums.sort(): {nums}")
print(divide)

t = (3, 2, 15, 10)  # tuple object has no attribute sort
print(sorted(t))  # the tuple becomes a list to sort it
tuple(t)  # this changes it back to a tuple
print(t)
print(divide)

d = {
    1: "Joe",
    3: "John",
    5: "Jenny",
    2: "Jessica",
    4: "Jerry",
}  # dict object has no attribute sort
sorted_dict = sorted(d) # returns a list
print(f"sorted_dict: {sorted_dict}")  # the keys are put in a list and sorted
print(f"original dict ref d: {d}")
print(divide)


"""
The following for loop prints the values in order of the sorted keys
"""
for i in sorted_dict:
    print(d[i])
print(divide)

example = {1: ["1", "one"], 2: ["2", "two"]}

ex_copy = example.copy()
print(example)
print(ex_copy)
print(divide)

example[2] = ["2", "two", "TWO"]
print(example) # this points to the new list
print(ex_copy) # this points to the original list
print(divide)

# BUT WATCH OUT FOR THIS...when the list contains a REFERENCE and the reference is changed, it changes for both
# the original and copied list
listC = []
listA = ["a", "b", "c"]
listB = ["x", "y", "z"]
listA[1] = listB
print(f"listA after assignment of B: {listA}")

listC = listA.copy()
print(f" initial listC: {listC}")

listB.append("rst")
print(f"listA after inner list (B) update:{listA}")
print(f"listC after inner list (B) update:{listC}")


# Basic deep copy example
names = {}
names["A"] = ["Alice", "Alvin"]
names_deep_copy = copy.deepcopy(names)
names["B"] = ["Beatrice", "Bartholomew"]
print(names)
print(names_deep_copy)

names["A"] = ["Alfred", "Adeline"]
print(names)
print(names_deep_copy)
print(divide)


# Deep copy with object reference
print(f"names before deep copy with reference:{names}")
names["C"] = ["Cindy", "Charles"]
 # should not change names_deep_copy
print(f"names AFTER append:{names}")
print(f"names_deep_copy after append:{names_deep_copy}")
print(divide)
