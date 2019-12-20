l = []
striped_l = []
while True:
    n = input()
    if n == '-1':
        break
    l.append(n)

for i in l:
    if i.count('=') > 1:
        i = i.split('=')
        i[0] = i[0].strip()
        i[1] = i[1].strip()        
        i[2] = i[2].strip()
        j = i[0] + '=' + i[1] + ' = ' + i[2]    
    else:
        i = i.split('=')
        i[0] = i[0].strip()
        i[1] = i[1].strip()
        j = i[0] + '=' + i[1]
    striped_l.append(j)
most = 0
for i in striped_l:
    if i.find('=') > most:
        most = i.find('=')



for i in l:
    #if i[0] == '=':
        #print(' '.rjust(most,' '),end='')
    if i.count('=') > 1:
        i = i.split('=')
        i[0] = i[0].strip()
        i[1] = i[1].strip()
        i[2] = i[2].strip()
        print(i[0].ljust(most,' '),end= ' ')
        print('= ',end= '')
        print(i[1],end= ' ')
        print('= ',end= '')
        print(i[2])
        
    else:
        i = i.split('=')
        i[0] = i[0].strip()
        i[1] = i[1].strip()
        print(i[0].rjust(most,' '),end= ' ')
        print('= ',end= '')
        print(i[1],)
        
    