n = input()
ls = []
out = []
i = 0
while i < len(n):
    ls.append(n[i:i+2])
    i += 1
for i in ls:
    i = i.lower()
    out.append(i)
out.sort()
out = list(dict.fromkeys(out))
for i in out:
    if len(i) == 2:
        print(i)
        