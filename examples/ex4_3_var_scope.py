

# Shadowing
msg = "Hello from the outside!"

def greet():
    msg = "Hellow from inside the function"
    print(msg)

greet()
print(msg)


# global
def change_message():
    # use 'global' keyword to indicate we want to work with the outer variable
    global msg
    msg = "The global message has been changed from the inside!"
    print("Inside the function:", msg)

print("-" * 50)
print("Before change_msg function call:", msg)
change_message()
print("After function call:", msg)