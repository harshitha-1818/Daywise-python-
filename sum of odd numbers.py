#sum of odd numbers
n=int(input("enter n value"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
         print(i,"is an odd number")
         sum +=i
print(sum)  