target = 72
x = 1
while True:
    num = int(input("Enter your guess: "))
    if num > 100 or num < 0:
        print("Sorry, your guess is out of range.")
    elif num == target:
        break
    elif num > target:
        print("Sorry, your guess is too high.")
    elif num < target:
        print("Sorry, your guess is too low.")
    x += 1
print("Congratulations, your guess is correct.")
print("Total number of guesses is {0}.".format(x))