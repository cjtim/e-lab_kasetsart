TV = int(input('How many TVs? '))
DVD = int(input('How many DVD players? '))
Audio = int(input('How many Audio Systems? '))
sum = TV*6000 + DVD*1500 + Audio*3000
if sum >= 24000:
    discount = sum*0.2
    print("Total price is {0:.2f} baht.".format(sum))
    sum = sum*0.8
    print("You've got a discount of {0:.2f} baht.".format(discount))
    print("Your payment is {0:.2f} baht. Thank you!".format(sum))
elif sum < 24000:
    print("Total price is {0:.2f} baht.".format(sum))
    print("Your payment is {0:.2f} baht. Thank you!".format(sum))