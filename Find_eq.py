## you can use print for debugging purposes, e.g.
## print "this is a debug message"
#
#def solution(A):
#    # write your code in Python 2.7
#    pass
#    A={-1, 3, -4, 5, 1, -6, 2, 1}
#    N=len(A)
#    
#    low = 0
#    high = N #7
#    P = (low+high)/2 #3
#    
#    sum_low_ele = 0
#    sum_up_ele = 0
#    flag =0
#    while flag==0:
#        i=0
#        for a in A :
##            print str(a)
#            if(i<P):
#                sum_low_ele += a
#            elif(i>P):
#                sum_up_ele += a
# #           print(str(i),str(a), str(sum_low_ele), str(sum_up_ele))
#            i+=1
#        if(sum_low_ele == sum_up_ele):
#            flag=1
#        elif(sum_low_ele < sum_up_ele):
#            P=((low+high)/2)+1
#        else:
#            P=((low+high)/2)-1
##    sum_ele = sum_low_ele + sum_up_ele #0
#    if P==0 or P==N-1:
#        sum_ele=0  
#    if P>N:
#        P = -1
#    print(str(P))
##    return P

#[1, 3, 7]
#Invalid result type, int expected, <type 'NoneType'> found.
#RUNTIME ERROR (tested program terminated unexpectedly) 
#A=input()
#print[i for i in range(len(A))if sum(A[:i])==sum(A[i+1:])]or-1

#25%Your code is syntactically correct and works properly on the example test.
#def solution(A):
#    # write your code in Python 2.7
#    pass
#    total_sum = sum(A)
#    prev, curr = 0, A[0]
#
#    for index in range(1, len(A)):
#        prev += A[index - 1]
#        curr += A[index]
#
#        if prev + curr == total_sum:
#            return index
#
#    return -1



#75%Your code is syntactically correct and works properly on the example test. 
def equi(A):
    if A==[]:
        return -1
    length=len(A)
    mid=length//2
    s=sum(A)
    if s-A[0]==0:
        return 0
    if s-A[length-1]==0:
        return length-1
    for i in range(length)[1:length-1]:
        si=s-A[i]
        if i<mid:
            if si==sum(A[:i])*2:
                return i
            else:
                if si==sum(A[i+1:])*2:
                    return i
    return -1
