print("First fraction:")
a = int(input("Enter a numerator a: "))
b = int(input("Enter a denominator b: "))
print("Second fraction:")
c = int(input("Enter a numerator c: "))
d = int(input("Enter a denominator d: "))
p = (a*d)+(b*c)
q = b*d

#from fractions import Fraction
#sum = Fraction(a, b) + Fraction(c, d)
#print("Summation of the two fractions is", sum)

print("Summation of the two fractions is", p, "/", q)
