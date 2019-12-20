#https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

#def fibo(n):
    #if n == 1 or n == 2:
        #return 1
    #else:
        #return fibo(n-1)+fibo(n-2)
def fibo(n): 
    a = 1
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 1 or n == 2: 
        return a
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b         
        
n = int(input("Enter n: "))
print("fibo(%d) = %d"%(n,fibo(n)))