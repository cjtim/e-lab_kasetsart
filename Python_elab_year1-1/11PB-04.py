n = input()
d = len(n)
correct = 0
pre_correct = 0
while True:
    guess = input()
    if guess == '0':
        break
    if guess in n :
        count = n.count(guess)
        n = n.replace(guess,'')
        correct += count
        
        
print('{0}/{1}'.format(correct,d))