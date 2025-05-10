a = 5 # Binary: 0101
b = 3 # Binary: 0011

# Bitwise AND
result_and = a & b # Binary: 0001
print(f"Binary of a: {bin(a)}")
print(f"Binary of b: {bin(b)}")
print(f"a & b:         {result_and} (Binary: {bin(result_and)})")
# Only the rightmost bit is 1 in both a and b, so the result has 1 in that position.

# Bitwise OR (|)
result_or = a | b
print(f"a | b:          {result_or} (Binary: {bin(result_or)})")
# If a bit is 1 in either a or b (or both), the result has 1 in that position.

# Bitwise XOR (^)
result_xor = a ^ b
print(f"a ^ b:         {result_xor} (Binary: {bin(result_xor)})")
# If the bits in a and b are different, the result has 1 in that position.

# Bitwise NOT (~)
result_not_a = ~a
print(f"~a:            {result_not_a} (Binary: {bin(result_not_a)})")
# This flips all the bits. Be mindful of Python's representation of negative numbers using two's complement.

# Left Shift (<<)
result_left_shift = a << 2
print(f"a << 2:        {result_left_shift} (Binary: {bin(result_left_shift)})")
# The bits of 'a' are shifted two places to the left, and two zeros are added on the right. This is equivalent to multiplying by 2 raised to the power of the shift amount (5 * 2^2 = 20).

# Right Shift (>>)
result_right_shift = a >> 1
print(f"a >> 1:        {result_right_shift} (Binary: {bin(result_right_shift)})")
# The bits of 'a' are shifted one place to the right. This is generally equivalent to integer division by 2 raised to the power of the shift amount (5 // 2^1 = 2).
