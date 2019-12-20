count = 0
max = 0
all_score = 0
n = abs(int(input()))
score = 0
more_40 = 0
while count < n :
    score = float(input())
    if score > 40 :
        max = score
        more_40 = more_40 + 1
    all_score = all_score + score
    count = count + 1

average = all_score/count
print("{0:.2f} {1}".format(average,more_40))