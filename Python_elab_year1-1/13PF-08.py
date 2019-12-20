n = int(input())
i = 0
ls = []
while i < n:
    num = int(input())
    ls.append(num)
    i += 1
ls.sort()

lowest = ls[1] - ls[0]
i = 0
while i < len(ls)-1:
    front = ls[i+1] - ls[i]
    if front < lowest:
        lowest = front
        index = i
    i += 1
print('{} {}'.format(ls[index],ls[index+1]))