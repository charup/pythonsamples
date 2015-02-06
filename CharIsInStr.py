def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    lenStr = len(aStr)
    print(lenStr)
    char = char.upper()
    aStr = aStr.upper()
    if(aStr==''):
        return False
        
    if(lenStr == 1):
        return (char == aStr)
        
    if(aStr[lenStr/2] == char):
        return True
        
    elif(char<aStr[lenStr/2]):
        return isIn(char, aStr[0:lenStr/2])
        
    elif(char>aStr[lenStr/2]):
        return isIn(char, aStr[lenStr/2+1:])
        
    else:
        return False

ans = isIn('s','String')
print ans