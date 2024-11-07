balance=20000
withdraw=int(input("enter a amount :"))
if(balance>withdraw):
    print("take the cash")
    print("the balance in account:",balance-withdraw)
else:
    print("insufficient money to withdraw")