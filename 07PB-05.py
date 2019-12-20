j = 1
prime = 0
while True:
    j = 1
    prime = 0
    num = int(input('Enter a number: '))
    if num == 0 :
        break
    if num <= 1 :
        print('Invalid input, try again.')
        prime = 0
    while j <= num:
        if num  % j == 0:
            prime += 1
        j += 1
    if prime == 2:
        print("{0} is a prime number.".format(num))
    elif prime > 2:
        print("{0} is not a prime number.".format(num))
    elif prime == 0:
        prime = 0
print('End of program, goodbye.')