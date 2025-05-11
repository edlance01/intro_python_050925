"""
You can create factories that produce functions with specific pre-configured behavior.
useful when you need several functions that perform a similar operation but with different parameters. Instead of defining each function explicitly, you can use a factory to generate them.
"""

def create_multiplier(factor):
    """Returns a function that multiplies its input by the given factor."""
    return lambda x: x * factor


multiply_by_5 = create_multiplier(5)
multiply_by_10 = create_multiplier(10)

print(multiply_by_5(3))
print(multiply_by_10(4))