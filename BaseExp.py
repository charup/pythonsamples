def iterPower(base, exp):
    if(base<0 and exp%2!=0):
        result = -1.0
    else:
        result = 1.0
    while(exp>0):
        result *= float(base)
        exp = int(exp)-1.0;
        print(str(result))
    return result

base =0;
exp = 0;
base = raw_input("Base:")
exp = raw_input("Exponent:")
result = iterPower(base, exp)
print("Power value :"+str(result))