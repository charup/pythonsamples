def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    print aStr
    if aStr[:] == '':
        return 0
    else:
        return lenRecur(aStr[1:])+1

length = lenRecur('String')#'Ab')#
print length