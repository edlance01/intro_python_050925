
d = 25
h = 0x12AB
o = 0o23
b = 0b0101

'''
When you do math with hexadecimal, octal, and binary, you always get a decimal (base 10) result.
When you do division, the result is a float.
'''
print(h + h) # prints 9558
print(h + b) # prints 4784
print(h + o) # prints 4798
print(o + b) # prints 24
print(d / b) # prints 5.0
print(h / o) # prints 251.52631578947367

print(d) # prints 25
print(h) # prints 4779
print(o) # prints 19
print(b) # prints 5

print(hex(4779)) # prints 0x12ab
print(oct(19)) # prints 0o23
print(bin(5)) # prints 0b101