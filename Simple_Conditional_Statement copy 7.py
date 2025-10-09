print("What area would you like to calculate?")
option = input("Choose: type T for triangle, type C for circle ")

if option == "T" or option == "t":
    print("You chose triangle")
    base = int(input("Give me the base: "))
    height = int(input("Give me the height: "))
    area1 = (base*height)/2
    print("The base of your triangle is ", area1)

elif option == "C" or option == "c":
    print("You chose circle")
    radius = int(input("Give me the radius: "))
    area2 = radius**2*3.14159
    print("The area of your circle is ", area2)

else:
    print("Can't follow your petition, try again")