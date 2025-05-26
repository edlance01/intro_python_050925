"""
You can use functions that return other functions to implement the Strategy design pattern, where you can easily switch between different algorithms or strategies at runtime.
"""
def create_comparison(compare_by):
    if compare_by == "name":
        return lambda person1, person2: person1["name"] > person2["name"]
    elif compare_by == "age":
        return lambda person1, person2: person1["age"] > person2["age"]
    else:
        return lambda p1, p2: False


people = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]

compare_by_name = create_comparison("name")
print(compare_by_name(people[0], people[1]))  # Output: True (Bob > Alice)

compare_by_age = create_comparison("age")
print(compare_by_age(people[0], people[1]))  # Output: True (30 > 25)
