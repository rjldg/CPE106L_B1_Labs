def mean(l):

    sum = 0
    
    for i in l:
        sum += i

    return 0 if len(l) == 0 else sum / len(l)

