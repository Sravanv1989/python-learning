#program to demonstrate input and output

#program to demonstrate input and output

cash=input('Enter your cash')
cashValue=int(cash)
#print('Type of cash:',type(cashValue))
atmAmount=60000
remainingAmount=atmAmount-cashValue
print('Take your cash',cash,'remainingAmount',remainingAmount,sep='->',end='===')
print('Thankyou for using ATM',end='\t')
print('visit again')
