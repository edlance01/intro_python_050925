#part 1
try:
    10/0
except(ZeroDivisionError):
    print("ZeroDivisionError")
except(ArithmeticError):
    print("ArithmeticError")

#part 2
def hi():
    try:
        print(int("Stephen"))
    except(ValueError):
        print("ValueError caught inside")

try:
    hi()
except(ValueError):
    print("ValueError caught outside")

#part 3
def hi():
    try:
        l = []
        d = {}

        l[0]
        d["1"]
    except(IndexError) as e:
        print(e)

try:
    hi()
except(LookupError) as e:
    print(e)