my_list = list(range(5))
print(my_list)  # [0, 1, 2, 3, 4]

letters = list("abcdfg")
print(letters)  # ['a', 'b', 'c', 'd', 'f', 'g']

# slicing
print(letters[1:4])  # ['b', 'c', 'd']

# get the length
print(f"The length of letters is {len(letters)}")

# append
letters.append("z")
print(f"letters after append:{letters}")

# extend
letters.extend(my_list)
print(f"letters after extending with my list of numbers: {letters}")
new_list = letters + my_list


# remove first occurence of 0
letters.remove(0)
print(f"letters after remove 0:{letters}")

# remove the 2nd entry in the list
letters.pop(1)
print(f"letters afer pop(1):{letters}")

# find the index of 'g'
location = letters.index("g")
print(f"g is in location:{location}")

# count occurences (add a couple of entries first)
letters.insert(4,"c")
letters.insert(6,"c")
print(letters.count("c"))