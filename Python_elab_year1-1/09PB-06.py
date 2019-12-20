def altersum(n):
    i = 1
    summ = 0
    while i <= n:
        if i % 2 == 0:
            summ -= i
        if i % 2 == 1:
            summ += i
        i += 1
    return summ