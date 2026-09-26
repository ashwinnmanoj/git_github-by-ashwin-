#concept:variable,integration,operation,ifelse
#customers account balance
balance = 50000
withdraw = int(input("enter the amount"))
if withdraw<=balance:
    balance=balance-withdraw
    print("withdrawal has been succeded")
    print("remaining balance",balance)
else:
    print("insufficent bank balance")

60000