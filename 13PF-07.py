import math
damage = int(input())
zombie_health = input().split(' ')
out2 = []
count = 0
for i in zombie_health:
    i = int(i)
    n = math.ceil(i/damage)
    count += n
    out2.append(count)
print(count)
for i in out2:
    print(i , end=' ')

