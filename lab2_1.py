answer1 = input(
    "Are strings immutable?\na. Yes\nb. No\nc. What does immutable mean? \nEnter your answer: "
)
if answer1.lower() == "a":
    print(
        f"""You answered: {answer1}, which is correct!
        Strings are immutable, which means that they cannot be changed after creation. """
    )
elif answer1.lower() == "b":
    print(
        f"""You answered: {answer1}, which is incorrect:(
        Strings are immutable. Remember that you must reassign a string to alter its value. """
    )
elif answer1.lower() == "c":
    print(
        f"""You answered: {answer1}, which is incorrect:(
        I appreciate your honesty. Immutable means that strings cannot be changed after creation. """
    )
else:
    print("You have not entered a valid answer. ")

answer2 = input(
    "What does the input() function return?\na. a string\nb. an integer\nc. whatever type you put in\nAnswer: "
)
if answer2.lower() == "a":
    print(
        f"""You answered: {answer2}, which is correct!
        The `input()` function in Python always returns the user's input as a string, even if they enter numbers."""
    )
elif answer2.lower() == "b":
    print(
        f"""You answered: {answer2}, which is incorrect:(
        The `input()` function returns a string. If you need an integer, you have to convert the string using `int()`."""
    )
elif answer2.lower() == "c":
    print(
        f"""You answered: {answer2}, which is incorrect:(
        The `input()` function always returns a string. Python doesn't automatically detect the type of input."""
    )
else:
    print("You have not entered a valid answer for the second question.")


answer3 = input(
    "What is the function used to capitalize the first letter or the first word of a string?\na. capitalize()\nb. first()\nc. upper()\nd.title()\nAnswer: "
)
if answer3.lower() == "a":
    print(
        f"""You answered: {answer3}, which is correct!
        The `capitalize()` method returns a string where the first character is uppercase and the rest are lowercase."""
    )
elif answer3.lower() == "b":
    print(
        f"""You answered: {answer3}, which is incorrect:(
        There is no built-in string method called `first()` in Python."""
    )
elif answer3.lower() == "c":
    print(
        f"""You answered: {answer3}, which is incorrect:(
        The `upper()` method converts all characters in a string to uppercase, not just the first letter."""
    )
elif answer3.lower() == "d":
    print(
        f"""You answered: {answer3}, which is incorrect:(
        While `title()` capitalizes the first letter of each *word* in a string, `capitalize()` only capitalizes the first letter of the entire string."""
    )
else:
    print("You have not entered a valid answer for the third question.")
