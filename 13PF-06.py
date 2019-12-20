name = input()
n = int(input())
if n < 0:
    n = n % len(name)
elif n > 0 :
    n = n % len(name)
if n == 0 :
    print(name)
else:
    print(name[-n:]+name[:-n])