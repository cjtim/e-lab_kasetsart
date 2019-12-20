buffet = input('Enter your buffet choice: ')
if buffet == 'Korean' or buffet == 'korean':
    Wed = input('Is today Wednesday (yes/no)? ')
    if Wed == 'no':
        sum = 1500
    elif Wed == 'yes':
        sum = 1500*0.85
    print("Your payment is {0:.2f} Baht.".format(sum))
elif buffet == 'Japanese' or buffet == 'japanese':
    Wed = input('Is today Wednesday (yes/no)? ')
    if Wed == 'no':
        sum = 1000
    elif Wed == 'yes':
        sum = 1000*0.85
    print("Your payment is {0:.2f} Baht.".format(sum))
else:
    print("Sorry, there is no {} buffet.".format(buffet))