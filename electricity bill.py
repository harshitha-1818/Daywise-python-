n=int(input("enter no.of units:"))
if(n<50):
    bill= 120
elif(n>50 and n<=100):
    bill=120+(n-50)*2.89
elif(n>100 and n<=150):
    bill=120+(100-50)*2.89+(n-100)*3.83
elif(n>150 and n<=200):
    bill=120+(100-50)*2.89+(150-100)*3.83+(n-150)*4.56
elif(n>200 and n<=300):
    bill=120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(n-200)*5.34
elif(n>300 and n<=400):
    bill=120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(n-300)*5.99
elif(n>400 and n<=500):
    bill=120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(400-300)*5.99+(n-400)*6.89
elif(n>500 and n<=750):
    bill=120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(400-300)*5.99+(500-400)*6.89(n-500)*7.56
else:
    bill=120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(400-300)*5.99+(500-400)*6.89+(750-500)*7.56+(n-750)*8.73
print(bill)