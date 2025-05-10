"""
A generator function is a special kind of function that, instead of returning
a single value, returns an iterator object. This iterator can then be used to
retrieve a sequence of values one at a time.
"""

"""
yield is the keyword that indicates a function is a generator function.

When a yield statement is encountered:
  1. The execution of the function pauses
  2. The value specified after yield is returned to the caller
  3. The local state of the function is saved
    A. This includes variable bindings, the instruction pointer, the internal
        stack, and any exception handling.
  4. When the iterator request the next value (via next()), the function resumes
     execution where it left off.
"""


# Generator function
def generate_squares(limit):
    """Generates the squares of numbers from 0 up to, but not including, the limit."""
    num = 0
    while num < limit:
        print("About to yield")
        yield num ** 2
        print("After yield")
        num += 1


if __name__ == '__main__':
    squares_generator = generate_squares(5)
    print(f"Generator object: {squares_generator}")

    for square in squares_generator:
        print(square)

    print("-" * 50 + "\n")

    # you can also call next() function yourself
    print("\ncalling next()")
    squares_generator_two = generate_squares(3)
    print(next(squares_generator_two))
    print(next(squares_generator_two))
    print(next(squares_generator_two))
    try:
        print(next(squares_generator_two)) # This will raise a StopIteration error
    except StopIteration:
        print("End of iteration.")