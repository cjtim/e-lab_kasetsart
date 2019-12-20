n = input()
n = n.split(' ')
out = ''
for i in n:
    if i == 'for' or i == 'and' or i == 'with' or i == 'of':
        
        out += i + ' '
    else:
        i = i.title()
        out += i + ' '
print(out[:-1])
        