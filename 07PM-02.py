print("Upper left corner coordinate:")
x = (int(input("  << x axis: ")))
y = (int(input("  << y axis: ")))
east = (int(input("  << Eastern: ")))
south = (int(input("  << Southern: ")))


print("Enter a coordinate:")
x_location = int(input("  << x axis: "))
y_location = int(input("  << y axis: "))


if x_location > x and x_location < east and y_location > south and y_location < y:
    print(">>> ({0:.2f}, {1:.2f}) is inside the rectangle.".format(x_location,y_location))
else:
    print(">>> ({0:.2f}, {1:.2f}) is not inside the rectangle.".format(x_location,y_location))