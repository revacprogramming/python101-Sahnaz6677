largest=None
smallest=None
while True:
    num=input("enter the number")
    if num== "done":
        break
    try:
        n=int(num)
        if largest is None or largest<n:
            largest=n
        if smallest is None or smallest>n:
            smallest=n
    except:
        print("Invalid input")
print("Maximum is ",largest)
print("Minimum is",smallest)