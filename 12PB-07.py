n = input()
out = ''
big = 0
j= 0

for i in n:
    if j == 0:
        i = i.lower()
        j += 1
    elif i == '-':
        i = i.replace('-','')
        big =1 
    elif i == '_':
        i = i.replace('_','')
        big =1 
    elif i == '=':
        i = i.replace('=','')
        big =1 
    elif i == '.':
        i = i.replace('.','')
        big =1 
    elif i == '$':
        i = i.replace('$','')
        big = 1 
    elif big == 1:
        i = i.upper()
        big = 0        
    out += i

print(out)
        