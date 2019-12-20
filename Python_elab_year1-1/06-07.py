count = 0
num = int(input("Enter an 8-bit number: "))
numbits = ("{0:b}".format(x))
numbits = int(numbits)
while True:
    last = numbits%10
    numbits = numbits//10
    if last == 1:
        count += 1
    if numbits == 0:
        break
print("The number {0} has {1} non-zero bits".format(num,count))