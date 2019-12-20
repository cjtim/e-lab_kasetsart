height = int(input('Enter height: '))
width = int(input('Enter width: '))
if height <= 0 or width <= 0:
    print("Invalid input, program terminates.")
    
i = 1
j = 1
while height >= i :
    
    j = 1
    while width >= j :
        if i % 2 == 1:
            print('* ',end='')
            j += 1
        elif i % 2 == 0:
            print(' *',end='')
            j += 1
    print()
    i += 1