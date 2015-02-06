def out():
    ans = isVowel('A')
    if(ans == True):
        print("True")
        
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    vow = {'a', 'e', 'i', 'o', 'u'}
    
    if char in vow:
        return((str(char)=='a') \
        or (str(char)=='e')\
        or (str(char)=='i')\
        or (str(char)=='o')\
        or (str(char)=='u')
        or (str(char)=='A') \
        or (str(char)=='E')\
        or (str(char)=='I')\
        or (str(char)=='O')\
        or (str(char)=='U'))
    else:
        return False
    
