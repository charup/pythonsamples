#program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

#GIVEN VALUES
#balance
#monthlyPaymentRate
#annualInterestRate

#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

balance = 3926
annualInterestRate = 0.2
	      
Min_Monthly_pay=0#{}
Monthly_unpaid_bal={}
New_bal={}
total_paid = 0
balance2 = balance

Monthly_interest_rate = (annualInterestRate) / 12.0
month = range(0,12)

while(balance2>0):
    balance2 = balance
    Min_Monthly_pay+=10
    total_paid = 0
    for i in month :
        #print(balance, str(month),i)    
        #Min_Monthly_pay[i] = monthlyPaymentRate * balance
        #Min_Monthly_pay[i] = 10
        Monthly_unpaid_bal[i] = balance2 - (Min_Monthly_pay)
        balance2 = Monthly_unpaid_bal[i] + (Monthly_interest_rate * Monthly_unpaid_bal[i])
        #print("Month:"+str(i+1))
        #print("Minimum monthly payment:"+str(round(Min_Monthly_pay,2)))
        #print("Remaining balance:"+str(round(balance2,2)))
        total_paid+=Min_Monthly_pay
#print("Total paid:"+str(round(total_paid,2)))
#print("Remaining balance:"+str(round(balance2,2)))
print("Lowest Payment:"+str(Min_Monthly_pay))