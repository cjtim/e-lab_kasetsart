hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))

hour1=0
hour3=0
hour4=0
hour5=0
invaild = 0
while True:
    if minutes < 0 or minutes > 60:
        invaild = 1
        break
    if minutes > 0 and minutes < 60:
        hours = hours + 1 
        minutes = 0    
    if hours < 0 or hours > 20:
        invaild = 1
    break
while True:
    if invaild == 1:
        break
    if hours <= 2:
        hour1 = 0
    if hours >= 3 :
        hour3 = 20
    if hours >= 4:
        hour4 = 20
    if hours >= 5:
        hour5 = (hours-4)*50
    break
while True:
    if invaild==1 :
        break
    elif buyAmt >= 300 and buyAmt <= 3000:
        hour3 = 0
        hour4 = 0
    elif buyAmt >3000 :
        hour1 = 0
        hour3 = 0
        hour4 = 0
        hour5 = 0
    break
if invaild == 1:
    print("Invalid time.")
else:
    sum = hour1 + hour3 + hour4 + hour5
    if sum == 0:
        print('No charge, thanks.')
    else:
        print("Total amount due is {} Baht, thank you.".format(sum))