def find_mode(l):
    sort = []
    sort.append(l.count(0))
    sort.append(l.count(1))
    sort.append(l.count(2))
    sort.append(l.count(3))
    sort.append(l.count(4))
    sort.append(l.count(5))
    sort.append(l.count(6))
    sort.append(l.count(7))
    sort.append(l.count(8))
    sort.append(l.count(9))
    sort.append(l.count(10))   
    return print(sort.index(max(sort)))
    
l = []   
i = 0
while i < 20:
    n = int(input('Enter score: '))
    if n < 0 or n > 10 :
        print('Score is out of range.')
    else:
        l.append(n)
        i += 1
print('-----')
print('Original list:')
print(l)
print('Mode of scores:')
find_mode(l)