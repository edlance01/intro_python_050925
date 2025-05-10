

nums = []

for i in range(10):
    nums.append(i)

print(f"Nums after for loop:{nums}")

nums2 = [n for n in range(10)]
print(f"Nums2 after list comprehension:{nums2}")