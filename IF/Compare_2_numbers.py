a = int(input("Give me a number "))
b = int(input("Give me another number "))
c = int(input("Give me another number "))
if a>b:
    if a>c:
        print(a, "is the biggest")
    else:
        print(c, "is the biggest")
else:
    if b>c:
        print(b, "is the biggest")
    else:
        print(c, "is the biggest")