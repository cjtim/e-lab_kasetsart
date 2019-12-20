hour = int(input("Enter number of hours: "))
min = int(input("Enter number of minutes: "))
total = (hour*60) + min
import math
more2hr = (total-120)/60 
more2hr_1 = math.ceil(more2hr)
if hour < 0 or min < 0:
    print("Input Error!")
elif (total <= 15):
    print('No charge, thanks.')
elif (total > 15 and total <= 120):
    sum = 10
    print('Total amount due is',sum,'Bahts.')
elif (total > 120):     
    sum = 10 + (more2hr_1*10)
    print('Total amount due is',sum,'Bahts.')
