gcd = 0
sum_gcd = 0
import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
first = num1
sec = num2
#while True:
    #gcd1 = first % sec
    #sum_gcd = sum_gcd + gcd1
    ##set
    #first = sec
    #sec = gcd1
    #if first%sec == 0:
        #break
sum_gcd = math.gcd(num1,num2)

while True:
    lcm  = (num1*num2) // sum_gcd
    break
    
print("  >> gcd(%d, %d) =%7d" % (num1,num2,sum_gcd))
print("  >> lcm(%d, %d) =%7d" % (num1,num2,lcm))