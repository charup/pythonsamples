#program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

#GIVEN VALUES
#balance
#monthlyPaymentRate
#annualInterestRate

#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

balance = 320000
annualInterestRate = 0.2
	      
Monthly_unpaid_bal={}
total_paid = 0
epsilon = 0.01
balance2 = balance

Monthly_interest_rate = (annualInterestRate) / 12.0

Min_Monthly_pay=round((balance/12),2)#0.01#{}
#Max_Monthly_pay=0
Max_Monthly_pay=round(((balance*(1+ Monthly_interest_rate)**12) / 12.0),2)

month = range(0,12)
i=0
flag=0
while(round(balance2,2)!=0.01):#abs(total_paid-balance)>=epsilon):#
    Monthly_pay = ((Min_Monthly_pay + Max_Monthly_pay) / 2)
    #print 'Monthly pay: ' + str(Monthly_pay)
    balance2 = balance
    total_paid = 0
    for i in month :
        Monthly_unpaid_bal[i] = balance2 - (Monthly_pay)
        balance2 = Monthly_unpaid_bal[i] + (Monthly_interest_rate * Monthly_unpaid_bal[i])
        total_paid+=Monthly_pay
#        print("Total paid:"+str(round(total_paid,2)))
    #print 'Remaining balance: ' + str(balance2) + ' Low: ' + str(Min_Monthly_pay) + ' High: ' + str(Max_Monthly_pay)
    if(round(balance2,2) == 0.01):
        #print 'Balance paid'
        break
    else:
        if(round(balance2, 2) > 0.01):
            #print 'Balance is not sufficient' + ' Total paid: ' + str(total_paid) + ' Balance: ' + str(balance2)
            Min_Monthly_pay = Monthly_pay
            #print 'Increasing the lower limit: '  + str(Min_Monthly_pay)
        elif(round(balance2, 2) < 0.01):
            #print 'Balance is too high' + ' Total paid: ' + str(total_paid) + ' Balance: ' + str(balance2)
            Max_Monthly_pay = Monthly_pay
            #print 'Reducing the upper limit: ' + str(Max_Monthly_pay)
print("Lowest Payment:"+str(round(Monthly_pay,2)))