import math
age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
if age < 15 or age > 60:
    print("Invalid age.")
elif income < 1 or income >= 80000:
    print("Invalid income.")
elif income >= 1 and income <= 30000:
    sum = income*(20/100)
    print("Your negative income tax is %.2f Baht."%sum)
elif income > 30000 and income < 80000:
    sum = 30000*(20/100) - (income-30000)*(12/100)
    print("Your negative income tax is %.2f Baht."%sum)
