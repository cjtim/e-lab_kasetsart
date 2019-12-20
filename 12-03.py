l = ''
i = 1
while True:
    n = input()
    if n == '':
        break
    if i % 2 == 1:
        l += max(n)
        
    else:
        l += min(n)
    i += 1
print(l)