# x first sunday in January
# n week
x = (input())
n = int(input())
if x == 'Sunday' :
    x = 1
elif x == 'Monday' :
    x = 2
elif x == 'Tuesday' :
    x = 3
elif x == 'Wednesday':
    x = 4
elif x == 'Thursday':
    x = 5
elif x == 'Friday':
    x = 6
elif x == 'Saturday':
    x = 7
else:
    if n < 0 or n >31 or x != 'Sunday' or x!= 'Monday' or x!= 'Tuesday' or x!= 'Wednesday' or x!= 'Thursday' or x!= 'Friday' or x!= 'Saturday':
        x=1
        n=0
        print('ERROR')

day = ((n%7)+x+1+1)
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
elif day == 7:
    print('Saturday')
elif day == 0:
    day = 0