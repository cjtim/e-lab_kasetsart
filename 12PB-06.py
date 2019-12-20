n = input()
n = n.replace(',' , '')
if n.count('.') > 1:
    print('ERROR')


elif len(n) - n.rfind(',') > 2:
    print('ERROR')
else:
    print(n)