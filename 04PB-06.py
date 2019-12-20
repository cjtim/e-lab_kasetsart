#year = int(input('Enter year: '))
#if year%400 == 0:
    #print("{} is a leap year.".format(year))
#elif year%100 == 0 :
    #print("{} is not a leap year.".format(year))
#elif year%4 == 0 :
    #print("{} is a leap year.".format(year))
#elif year <= 0 :
    #print("Invalid year.")
#else :
    #print("{} is not a leap year.".format(year))
    
year=int(input("Enter year: "))
if year <= 0 :
    print("Invalid year.") 
elif(year%4==0 and year%100!=0 or year%400==0):
    print("{} is a leap year.".format(year))

else:
    print("{} is not a leap year.".format(year))

#year = int(input("Enter year: "))  
#if (year % 4) == 0:  
   #if (year % 100) == 0:  
       #if (year % 400) == 0:  
           #print("{0} is a leap year.".format(year))  
       #else:  
           #print("{0} is not a leap year.".format(year))  
   #else:  
       #print("{0} is a leap year.".format(year))  
#elif year <= 0 or year == 0:
    #print("Invalid year.") 
#else:  
   #print("{0} is not a leap year.".format(year))