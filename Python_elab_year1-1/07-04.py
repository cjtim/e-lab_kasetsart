import math
count = 0

num = int(input("Enter a number: "))
while count <= num:
     print("{0}! = ".format(count) , end="")
     count2 = count
     while count2 >= count:
          print("x {} ".format(count2),end="")
          count2 -= 1
     print("=",math.factorial(count))     
     count += 1
     