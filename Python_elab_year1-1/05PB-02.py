hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))

first = 0
tri_hour = 0
fourth_hour = 0
fifth_hour = 0
invaild = 0
while True:
    if hours < 0 or hours > 20:
        invaild = 1
        break
    if minutes < 0 or minutes >59 :
        invaild = 1
        break
    if minutes > 0 and minutes < 60:
        hours = hours + 1 
        minutes = 0
        break
    break
while True:
    if invaild == 1:
        break
    if hours >20:
        invaild = 1
        break
    if hours <= 2:
        sum = 0
    if hours >= 3 :
        tri_hour = 20
    if hours >= 4:
        fourth_hour = 20
    if hours >= 5:
        fifth_hour = (hours-4)*50
    break

while True:
    if invaild==1 :
        break
    elif buyAmt < 300 :
        break
    elif buyAmt >= 300 and buyAmt <= 3000:
        tri_hour = 0
        fourth_hour = 0
        break
    elif buyAmt >3000 :
        first = 0
        tri_hour = 0
        fourth_hour = 0
        fifth_hour = 0
        break
if invaild == 1:
    print("Invalid time.")
else:
    sum = first + tri_hour + fourth_hour + fifth_hour
    if sum == 0:
        print('No charge, thanks.')
    else:
        print("Total amount due is {} Baht, thank you.".format(sum))