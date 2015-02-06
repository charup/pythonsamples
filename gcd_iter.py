def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if(b==0):
        return a
    else:
        return gcdRecur(b, a%b)
        
base =0;
exp = 0;
result = gcdRecur(2,12)#-224362718.2212
print("GCD :"+str(result))