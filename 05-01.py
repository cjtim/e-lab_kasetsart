#n = 99
#while n >= 51 :
    #print(n)
    #n = n - 2

last = int(input())
start = 0
print(start)
while start <= last:
    if last % 3 == 0:
        start = start + 1
        print(start)
        start = start +1
        print(start)
        start = start + 1
    else :
        start = start + 1
        print(start)
        start = start + 1
        if start <= last :
            print(start)
        start = start + 1