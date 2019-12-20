l = int(input('Enter level pokemon: '))
ball = (input('Enter level pokeball: '))
d = int(input('Enter distance: '))
if l >= 0 and l <=40 :
    if ball == 'l' or ball == 'L':
        x = 0.05
    elif ball == 'm' or ball ==  'M' :
        x = 0.03
    elif ball == 'h' or ball == 'H' : 
        x = 0.01
if l >= 41 and l <= 60 :
    if ball == 'l' or ball == 'L':
        x = 0.03
    elif ball == 'm' or ball == 'M' :
        x = 0.05
    elif ball == 'h' or ball ==  'H' : 
        x = 0.01
elif l >= 61 and l <= 100:
    if ball == 'l' or ball == 'L':
        x = 0.1
    elif ball == 'm' or ball == 'M' :
        x = 0.08
    elif ball == 'h' or ball == 'H' :    
        x = 0.01
s = 100 - (l * d * x)
if s < 0 :
    s = 0
elif x >= 100:
    s = 100
else :
    s = s
print('{0:.2f} percent.'.format(s))