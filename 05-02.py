count = 0
low = 0
hi = 1
all = 0
i = 0
n = input()

if n == '':
    i = 1
else:
    n = int(n)
    n = abs(n)
    low = n
    hi = n
    count = count + 1
    all = all + n

while i < 1:
    n = str(input())
    if n == '':
        i = 1
    elif n != '':
        n = int(n)
        n = abs(n)
        if n < low:
            low = n
        elif n > hi:
            hi = n 
        count = count + 1
        all = all + n
    else:
        print('ERROR')

print("{0:.2f} {1:.2f}".format(hi,low))
print("{0:.2f} {1:.2f}".format(all,all/count))