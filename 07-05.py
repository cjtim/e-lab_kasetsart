while True:    
    num = int(input("Enter a number: "))
    if num <= 1:
        if num == 0:
            print("End of program, goodbye.")
        else:
            print("Invalid input, try again.")
    loop2 = 1
    count = 0
    while num >= loop2:
        if num%loop2 == 0:
            #ลงตัว
            loop2 += 1
        if num/loop2 == 1:
            break
    break
print(count)