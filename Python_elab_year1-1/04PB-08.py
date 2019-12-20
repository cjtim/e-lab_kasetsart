import math
min = int(input("Minutes before due: "))
temp = float(input('Temperature: '))
rain = input('Is it raining (y/n)? ')
day = (min/(60*24))
day = abs(day)
from decimal import Decimal, ROUND_HALF_UP
day = Decimal(day).to_integral_value(rounding=ROUND_HALF_UP)

DO = '>>> I will do the assignment.'
NOT = '>>> I will not do the assignment.'

if day < 2 :
    print(">>> {} days before due.".format(day))
    print(DO)
    #if temp <= 40:
        #print(">>> {} days before due.".format(day))
        #print(DO)
    #elif temp > 40:
        #print(">>> {} days before due.".format(day))
        #print(NOT)
    #elif temp > 25 :
        #if (rain == 'Y' or rain == 'y'):
            #print(">>> {} days before due.".format(day))
            #print(NOT)
        #elif (rain == 'N' or rain == 'n'):
            #print(">>> {} days before due.".format(day))
            #print(DO)            
elif day >=2 and day <=5:
    if temp > 40:
        print(">>> {} days before due.".format(day))
        print(NOT)
    elif temp > 25 :
        if (rain == 'Y' or rain == 'y'):
            print(">>> {} days before due.".format(day))
            print(NOT)
        elif (rain == 'N' or rain == 'n'):
            print(">>> {} days before due.".format(day))
            print(DO)            
    else:
      print(">>> {} days before due.".format(day))
      print(DO)
elif day > 5:
    print(">>> {} days before due.".format(day))
    print(NOT)

