n = (input())
n_sorted = list(n)
count = 0
pre = 0

for i in n:
    if ord(i) > pre:
        pre = ord(i)
        count += 1
    elif ord(i) < pre:
        break
print(count)
