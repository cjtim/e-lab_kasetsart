num = int(input())
if num <= 0 :
    print('ERROR')
else:
    remain = 1
    while remain != 0 :
        last_digi = num % 10
        remain = num // 10
        num = remain 
        print(last_digi)
    