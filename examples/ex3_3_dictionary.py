

states = { "TX" : "Texas",
      "CA": "California",
      "PA": "Pennsylvania"}

# set a new value
states["GA"] = "Georgia"

for key in states.keys():
    print(key + "=" + states[key])

for value in states.values():
    print(value, end= ",")

print("\n*** get examples ***")
print(states.get("CA"))

print(states.get("ID", "unknown"))

print("-" * 50)
# items is handy to loop through keys and values
for k,v in states.items():
    print("The Key is ", k)
    print("The value is ", v)

