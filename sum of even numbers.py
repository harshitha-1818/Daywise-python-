#sum of even numbers
n=int(input("enter n value"))
sum=0
for i in range(1,n+1):
    if(i%2==0):
         print(i,"is an even number") 
         sum +=i
print(sum)  