n = input()
correct = []
out = ''
while True:
    guess = input()
    if guess == '0':
        break
    correct.append(guess)
for i in n:
    if i in correct :
        out += i
    else:
        out += '-'
print(out)
    