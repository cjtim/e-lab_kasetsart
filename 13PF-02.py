name1 = input()
name2 = input()

#Find_First_index
index1 = 0
j = 0
pre1 =0
for i in name1:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        pre1 = index1
        j += 1
    if j == 2:
        break
    index1 += 1

index2 = 0
pre2 = 0
for i in name2:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        pre2 = index2
        break
    index2 += 1
if pre1 == 0 and pre2 == 0:
    print(name1+name2)
elif pre1 == 0:
    print(name1+name2[pre2+1:])
elif pre2 == 0:
    print(name1[0:pre1]+name2)
else:
    print(name1[0:pre1]+name2[pre2+1:])
