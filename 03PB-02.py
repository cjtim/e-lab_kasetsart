money = float(input("Enter buying amount: "))
if(money >= 1000 and money < 3000):
    sum = money*(0.9)
elif (money >= 3000):
    sum = money*0.85
else:
    sum = money
print("Amount due after discount is",'{:.2f}'.format(sum),'baht.')
