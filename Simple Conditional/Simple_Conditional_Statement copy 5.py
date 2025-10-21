print("Consider the equation Ax+B=0")
a = int(input("Give me a number: "))
b = int(input("Give me a number: "))

if a == 0:
    print("No solution")
elif b == 0:
    print("Every real number can be a solution")
else:
    x = -b/a
    print("x is equal to: ", x)