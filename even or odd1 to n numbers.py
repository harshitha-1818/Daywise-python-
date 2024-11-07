#print even values from 1 to n numbers
n=int(input("enter n value"))
for i in range(1,n+1):
    if(i%2==0):
        print(i,"is an even number")
     
#print odd values from 1 to n numbers
n=int(input("enter n value"))
for i in range(1,n+1):
    if(i%2!=0):
        print(i,"is an odd number")
