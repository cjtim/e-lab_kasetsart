target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))
count = 0
correct = 0
while True:
    d = target%10
    target = target//10
    c = target%10
    target = target//10
    b = target%10
    target = target//10
    a = target%10
    break
while True:
    h = guess%10
    guess = guess//10
    g = guess%10
    guess = guess//10
    f = guess%10
    guess = guess//10
    e = guess%10
    break
while True :
    if a == h or a == e or a == f or a == g:
        count += 1
    if b == h or b == e or b == f or b == g:
        count += 1
    if c == h or c == e or c == f or c == g:
        count += 1
    if d == h or d == e or d == f or d == g:
        count += 1  
    if a == e:
        correct += 1
    if b == f:
        correct += 1
    if c == g:
        correct += 1
    if d == h:
        correct += 1
    break

if correct == 0:
    print("No positions correct, ",end="")
elif correct == 1:
    print("One positions correct, ",end="")
elif correct == 2:
    print("Two positions correct, ",end="")
elif correct == 3:
    print("Three positions correct, ",end="")
elif correct == 4:
    print("Congratulations, you just mastered my mind!!")

if count == 0:
    print("no digits correct")
elif count == 1:
    print("one digit correct")
elif count == 2:
    print("two digit correct")
elif count == 3:
    print("three digit correct")
elif count == 4:
    print("four digit correct")
    
