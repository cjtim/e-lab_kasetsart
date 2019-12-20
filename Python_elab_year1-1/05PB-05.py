h = int(input("Enter height: "))
i = 1
while i <= h:
    if i == 1 :
        print((2*h-2*i)*' '+'1')
        i += 1
    else:
        print((2*h-2*i)*' '+'1'+' '*(4*(i-1)-1)+'1')
        i =i + 1
