def mode(l):

    '''
    # Traditional method
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
    '''

    # More optimized solution to get mode using hashmap

    modes = {element: l.count(element) for element in l}
    mx = 0
    mx_int = None
    temp = []

    for element, count in modes.items():
        if count > mx:
            temp.clear()
            mx = count
            mx_int = element
            temp.append(mx_int)
        elif count == mx:
            temp.append(element)
            mx_int = None

    return mx_int if mx_int is not None else temp
    
        