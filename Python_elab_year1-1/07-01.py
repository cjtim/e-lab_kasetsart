count = 0
count2 = 0
character = 65

num = int(input("Enter a number: "))
if num <=0 or num > 26:
    print("Invalid input, program terminates.")
else:
    while count < num:
        count2 = 0
        while count2 <= count:
            print(chr(character), end='')
            character += 1
            count2 += 1
        count += 1
        print()
        character = 65
    
         
