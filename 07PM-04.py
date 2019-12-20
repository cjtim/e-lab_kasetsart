import math
while True:
    print("<<Point a>>")
    a_x = int(input("Enter x coordinate: "))
    a_y = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    b_x = int(input("Enter x coordinate: "))
    b_y = int(input("Enter y coordinate: "))
    if a_x == 0 and a_y == 0 and b_x == 0 and b_y == 0:
        print("Goodbye")
        break
    summ = math.sqrt((a_x-b_x)**2+(a_y-b_y)**2)
    print("Distance between ({0}, {1}) and ({2}, {3}):".format(a_x,a_y,b_x,b_y))
    print("Euclidean distance is {0:.2f}.".format(summ))
    horizon = b_x-a_x
    print("Horizontal distance is {}.".format(abs(horizon)))
    vertical = b_y-a_y
    print("Vertical distance is {}.".format(abs(vertical)))
    if horizon-vertical == 0 :
        print("We are going nowhere.")
    elif horizon == 0 and vertical > 0:
        print("We are going north.")
    elif horizon == 0 and vertical < 0 :
        print("We are going south.")
    elif horizon > 0 and vertical == 0 :
        print("We are going east.")
    elif horizon < 0 and vertical == 0:
        print("We are going west.")
    #may_break
    elif horizon > 0 and vertical > 0:
        print("We are going north-east.")
    elif horizon < vertical and horizon < 0 and vertical > 0:
        print("We are going north-west.")
    elif horizon > 0 and vertical < 0:
        print("We are going south-east.")
    elif horizon < 0 and vertical < 0:
        print("We are going south-west.")