s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
hour = (s1+s2)//3600
min = ((s1+s2)%3600)//60
sec = (s1+s2)%60
print("It is", hour, "hours", min, "minutes and", sec, "seconds.")
