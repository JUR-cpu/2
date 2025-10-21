a = int(input("Give me a number: "))
b = int(input("Give me a number: "))
if a%b == 0:
    print("The division is exact. Quotient: ", a/b)
else:
    print("The division is not exact. Quotient: ", int(a/b), "Residue:", a%b)
