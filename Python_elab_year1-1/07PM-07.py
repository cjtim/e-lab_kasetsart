# x first sunday in January
# n week
x = int(input())
n = int(input())
if x >= 8 or x <= 0 or n < 0 or n >31:
    print('ERROR')
else:
    day = (n-x+1)%7
    if day == 1:
        print('Sunday')
    elif day == 2:
        print('Monday')
    elif day == 3:
        print('Tuesday')
    elif day == 4:
        print('Wednesday')
    elif day == 5 :
        print('Thursday')
    elif day == 6:
        print('Friday')
    elif day == 0:
        print('Saturday')