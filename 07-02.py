count = 0
count2 = 0
character = 65

num = int(input("Enter a number: "))
num2 = num
if num <=0 or num > 26:
    print("Invalid input, program terminates.")
else:
    while count < num:
        count2 = 0
        
        while count2 < num2:
            print(chr(character), end='')
            character += 1
            count2 += 1
        
        
        count += 1
        print()
        character = 65
        num2 -= 1
    
         
