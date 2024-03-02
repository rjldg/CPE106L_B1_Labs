def mode(l):

    if len(l) == 0:
        return 0
    
    mx = -1
    tempSet = set(l)
    eqMode = False

    for i in tempSet:
        c = l.count(i)
        if(c > mx):
            mx = c
            temp = i
            eqMode = False
        elif(c == mx):
            eqMode = True
    
    if eqMode:
        return -1
    
    return temp