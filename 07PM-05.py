count = 0
num = int(input("Enter a number: "))
digi = int(input('Enter a digit: '))
if num < 0:
    print('Invalid number.')
if digi < 0 or digi > 9:
    print('Invalid digit.')    
if num >= 0 and (digi >= 0 and digi <= 9):  
    while True:
        last = num%10
        num = num // 10
        if last == digi:
            count += 1
        if num == 0 :
            if count == 1:
                print('Digit {0} occurs {1} time.'.format(digi,count))
            else:
                print('Digit {0} occurs {1} times.'.format(digi,count))
            break
        