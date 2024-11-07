#count of individuals
n = int(input("enter n value"))
count = 0 
if n>=0:
    print(1)
else:
 while n>=0:
    count=count+1
    n=n//10
 print(count)
