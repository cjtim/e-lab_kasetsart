last = 0
summ = 0

num = int(input())
while True:
    last = num%10
    summ = summ + last
    num = num//10
    
    
    if num == 0:
        if summ//10 != 0:
            num = summ
            summ = 0
            last = 0
            continue
        else:
            break
print(summ)