num = int(input())
summ = 1
last = 0
while True:
    last = num % 10
    if last % 2 == 0:
        summ = summ * last
    num = num // 10
    if num == 0 :
        summ = summ + num
        if summ == 1:
            summ = -1
        print(summ)
        break