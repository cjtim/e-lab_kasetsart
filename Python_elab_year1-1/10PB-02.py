l =[]
total = 0
def accum_sum(l):
    print("Original list:")
    print(l)
    print('Accumulative Sum:')
    total = 0
    for x in l:
        total = total + x
        print(total)
    
    
while True:
    n = int(input("Enter a number (0 to end): "))
    if n == 0:
        break
    if n < 0 or n > 999:
        print('Number is out of range.')
    else:
        l.append(n)
accum_sum(l)