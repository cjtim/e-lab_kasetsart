num = int(input())
num1 = 1
num2 = 1
store = 100000000000000000000000000000000
while num1 < num:
    while num2 <= num:
        if num1 * num2 == num:
            summ = num1 + num2
            if summ < store:
                store = summ
        num2+= 1
    if num1 * num2 == num:
        summ = num1 + num2
        if summ < store:
            store = summ    
    num1 += 1
    num2 = 0
print(store)
    
        
        
#add num1 til == num
#add num2 += 1