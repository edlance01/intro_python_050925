"""
Decorators in Python are a syntactic sugar for wrapping functions. They are often implemented using functions that return other functions.

Decorators allow you to add functionality to existing functions (like logging, authentication, or formatting) without modifying their core logic. This promotes code reuse and keeps your functions focused on their primary tasks.
"""
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"

    return wrapper


@bold_decorator
def get_name(name):
    return name


print(get_name("Alice"))  # Output: <b>Alice</b>
