import math
KM = int(input())
L = int(input())
n1 = (((KM/15)/L)/0.5)
if (KM/15)%L == 0:
    n1 = n1 + 1
n11 = math.ceil(n1)
print(n11)

n2 = (((KM/15)/L)/0.9)
if (KM/15)%L == 0:
    n22 = n2 + 1
n22 = math.ceil(n2)
print(n22)