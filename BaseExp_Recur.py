def recurPower(base, exp):
    if(exp>0):
        return base * recurPower(base, exp-1)
    elif(exp==0):
        return 1.0
        
base =0;
exp = 0;
#base =int( raw_input("Base:"))
#exp = int(raw_input("Exponent:"))
#print (type(base),type(exp))
#result = recurPower(base, exp)
result = recurPower(-3, 3)
print("Power value :"+str(result))


def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if(exp>0 and exp%2==0):
        return recurPowerNew(base*base,exp/2)#(base*base)**(exp/2)
    elif(exp>0 and exp%2==1):
        return base*recurPowerNew(base,exp-1)#(base*(base**(exp-1)))
    elif(exp==0):
        return 1
        
base =0;
exp = 0;
result = recurPowerNew(-8.47, 9)#-224362718.2212
print("Power value :"+str(result))
