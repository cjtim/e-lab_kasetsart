i = 0
score = []
while i < 20:
    data = int(input("Enter score: "))
    if data <0 or data > 10:
        print("Score is out of range.")
        continue
    score.append(data)
    i += 1
    
print('Original list:')
print(score)
print('',0, score.count(0)*'*')
print('',1, score.count(1)*'*')
print('',2, score.count(2)*'*')
print('',3, score.count(3)*'*')
print('',4, score.count(4)*'*')
print('',5, score.count(5)*'*')
print('',6, score.count(6)*'*')
print('',7, score.count(7)*'*')
print('',8, score.count(8)*'*')
print('',9, score.count(9)*'*')
print(10, score.count(10)*'*')
