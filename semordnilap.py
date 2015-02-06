def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    print str1, str2
    tempStr = str2[::-1] # reverse string
    length1 = len(str1)
    length2 = len(str2)
    iterations = min(length1,length2)
    if length1 != length2:
        return False
    if str1[0] == tempStr[0]:#length2-1]:
        return True
    else:
        return False
    if(iterations != 0):
        return semordnilap(str1[0:iterations-1], str2[1:])
        
result = semordnilapWrapper('tact','cat')
print result

    ## Your code here
    #length1 = len(str1)
    #length2 = len(str2)
    #if(length1!=length2):
    #    return False
    #if(length2 == 0):
    #    return True
    #if (str1[0] == str2[length2-1]):
    #    return semordnilap(str1[1:],str2[0:length2-1])
    #else:
    #    return False
        
"""//shorter by vasanth
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    print str1, str2
    tempStr = str2
    if str1[0] == tempStr[0] and str1 != '':
        return True and semordnilap(str1[0], str2[-1])
    if str1[0] != tempStr[0]:
        return False
    elif str1 == '' or str2 == '':
        return False

result = semordnilapWrapper('tact','cat')
print result
"""