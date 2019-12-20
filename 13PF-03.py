ls = input()
n = int(input())
ls = ls.split(',')
del ls[7]
ls = ls*((n//7)+1)
print(ls[n-1])