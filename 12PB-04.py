n = input()
j = 0
out = ''
plus = ''
filename = ''
n = n.replace("\\" , "_")
n = n.replace('/','_')
n = n.replace('*','_') 
n = n.replace(':','_')
n = n.replace("|",'_')
n = n.replace('"','_') 
n = n.replace('<','_')
n = n.replace('>','_') 
n = n.replace(' ','_') 

rmost = n.rfind('.')
n = n.replace('.' ,'_')
for i in n:
    if j == rmost:
        i = '.'
    out += i
    j += 1

out = out.split('.')

name = out[0]
if rmost == -1:
    name = name[:15]
    print(name)
else:
    filename = out[1]
    filename = filename[:3]    
    name = name[:15]
    print(name + '.' + filename)  