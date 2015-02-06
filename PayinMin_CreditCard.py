#program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month

#GIVEN VALUES
#balance
#monthlyPaymentRate
#annualInterestRate

#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      
Min_Monthly_pay={}
Monthly_unpaid_bal={}
New_bal={}
total_paid =0

Monthly_interest_rate = (annualInterestRate) / 12.0
month = range(0,12)

for i in month :
    #print(balance, str(month),i)    
    Min_Monthly_pay[i] = monthlyPaymentRate * balance
    Monthly_unpaid_bal[i] = balance - (Min_Monthly_pay[i])
    balance = Monthly_unpaid_bal[i] + (Monthly_interest_rate * Monthly_unpaid_bal[i])
    print("Month:"+str(i+1))
    print("Minimum monthly payment:"+str(round(Min_Monthly_pay[i],2)))
    print("Remaining balance:"+str(round(balance,2)))
    total_paid+=Min_Monthly_pay[i]
print("Total paid:"+str(round(total_paid,2)))
print("Remaining balance:"+str(round(balance,2)))
    