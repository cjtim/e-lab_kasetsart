l= ""
n = input()
for i in n:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                i = i.upper()
                #if i.islower():
                        #i = i.upper()
                        #l.append(i)
                        #continue
                #elif i.isupper():
                        #i = i.lower()
                        #l.append(i)
                        #continue
        else:
                i = i.lower()
        l += i
                
print(l)
        