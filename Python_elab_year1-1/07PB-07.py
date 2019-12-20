num = int(input('Enter positive integer: '))
if num <= 0:
    print('Invalid number.')
i = 0
prime = 2
while True:
    j = 2
    while j <= num :
        if num % j == 0:
            print(j)
            num = num / j
        else:
            j += 1
    break


#300/2 print
#150/2 print