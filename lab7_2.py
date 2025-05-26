
def divide():
    try:
        10/0
    except(ZeroDivisionError) as e:
        print("exception caught inside")
    else:
        print("no exception inside")
    finally:
        print("all done inside")

try:
    divide()
except(ZeroDivisionError) as e:
    print("exception caught outside")
else:
    print("no exception outside")
finally:
    print("all done outside")