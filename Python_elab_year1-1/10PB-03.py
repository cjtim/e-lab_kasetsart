import math
#l = []
l = [34.0, 80.5, 22.75, 56.0, 78.25, 92.25, 69.0, 78.5, 83.0, 46.75]
#count = 0
count = 10
def find_sd(l):
    sum_up = 0
    #up_sd
    for i in l:
        up = (i-average)**2
        sum_up += up
    #down_sd
    sum_down = count - 1
    return math.sqrt(sum_up/sum_down)
        
while True:
    n = float(input("Enter score: "))
    if n == -1 :
        average = sum(l)/count
        break
    elif n < 0 or n > 100:
        print("Score is out of range.")
    else:
        l.append(n)
        count += 1
print("Maximum score is {0:.2f}.".format(max(l)))
print('Minimum score is {0:.2f}.'.format(min(l)))
print('Average score is {0:.2f}.'.format(average))
print('Standard deviation is {0:.2f}.'.format(find_sd(l)))