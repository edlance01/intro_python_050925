import time

nums = []

for_start_time = time.time()
for i in range(1000):
    nums.append(i)
for_end_time = time.time()
print(f"Elapsed time FOR:{for_end_time - for_start_time}")

#print(f"Nums after for loop:{nums}")

print("-" * 50 + "\n")

comp_start_time = time.time()
nums2 = [n for n in range(1000)]
comp_end_time = time.time()
print(f"Elapsed time COMP:{comp_end_time - comp_start_time}")
#print(f"Nums2 after list comprehension:{nums2}")
