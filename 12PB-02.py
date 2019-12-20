n = input()

n = n.split(',')
out = '' 
j = 0
for i in n:
    i = i.strip()
    out += '"' + i + '"'
    out += ','
out = out[:-1]
print(out)
    