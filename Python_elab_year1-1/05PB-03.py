odd = 0
while True:
    num = int(input("Enter number: "))
    if num < 0:
        print("Received {} odd numbers".format(odd))
        break
    if num % 2 != 0:
        odd = odd + 1