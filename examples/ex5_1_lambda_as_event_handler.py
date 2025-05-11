# lambdas are great as customizable callbacks / actions
"""
Imagine you're building a system where different events need to trigger different actions. Instead of having a large conditional block to decide what to do, you can have a function that returns the appropriate action function based on the event type.
"""
def create_event_handler(event_type):
    if event_type == "login":
        return lambda user: print(f"User {user} logged in.")
    elif event_type == "logout":
        return lambda user: print(f"User {user} logged out.")
    elif event_type == "item_added":
        return lambda item: print(f"Item {item} added to cart.")
    else:
        return lambda _: print(f"Unknown event: {event_type}")

login_handler = create_event_handler("login")
logout_handler = create_event_handler("logout")
add_item_handler = create_event_handler("item_added")
unknown_handler = create_event_handler("unknown")

login_handler("Alice")
logout_handler("Bob")
add_item_handler("Book")
unknown_handler("delete_account")
