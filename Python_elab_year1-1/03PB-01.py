weight = float(input("Weight (kg): "))
height = float(input('Height (m): '))
BMI = weight/height**2
print('BMI is','%.1f'%BMI)
if BMI <= 18.5:
    print('Underweight')
elif (BMI < 25 and BMI >= 18.5):
    print('Normal weight')
elif (BMI >=25 and BMI <30):
    print('Overweight')
elif (BMI >= 30):
    print('Obesity')