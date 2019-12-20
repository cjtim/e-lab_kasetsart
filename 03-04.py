C= float(input())
TEXT = input()
F = (9/5)*C+32
K = C+273.15
if TEXT == 'f' or TEXT == 'F':
    print(F)

elif TEXT == 'k' or TEXT == 'K':
    print(K) 
else:
    print('ERROR')