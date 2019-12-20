def nb_year(p0, percent, aug, p):
    summ = 0
    i = 0
    while summ < p:
        if i == 0 :
            summ = int(p0 + (p0*(percent/100)) + aug)
            i += 1
        else:
            summ = int(summ + (summ*(percent/100)) + aug)
            i += 1
    return i