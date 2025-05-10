"""
Why and empty tuple?
"""

"""As a return value from a function: A function might need to return a tuple in certain situations. 
If, under some condition, there are no values to return, it might return an empty tuple. This provides 
a consistent data type.
"""
def process_data(data):
    if not data:
        return ()  # Return an empty tuple if no data
    #  ... process the data and return a tuple of results
    return (1, 2, 3)

"""
As a default argument: You can use an empty tuple as a default value for a function parameter.
"""
def my_function(values=()):
    if not values:
        print("No values provided.")
    else:
        print(f"Values: {values}")
my_function()  #output: No values provided
my_function((4,5,6)) #output: Values: (4, 5, 6)

"""
For consistency or initialization: In some cases, you might initialize a variable with an empty tuple to ensure
it's of the correct type, even if you plan to populate it later (though you'd have to assign a new tuple, not 
modify the original).

To represent the absence of data: Similar to returning an empty tuple, it can be used to explicitly indicate that there's no data to represent.

Interacting with APIs or external systems: Some APIs or external systems might require or return data in tuple format.
An empty tuple might be used to represent an empty response or a null value in such cases.
"""