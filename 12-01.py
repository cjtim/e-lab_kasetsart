string = ''
l = []
pre = ''
while True:
    n = input()
    if n == '':
        break
    l.append(n)
for i in l:
    if len(pre) < len(i):
        pre = i
print(pre)