program = input()
len_program = len(program)-2
test = input()
count = 1
for i in test:
    count += program.count(i)
    program = program.replace(i,'')
    test = test.replace(i,'')
    
print(count-1)
if len_program == 0 :
    len_program = 1
print('{0:.2f}'.format(((count-1)/(len_program))*100))
