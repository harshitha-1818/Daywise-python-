n=int(input("enter n value"))
num=1
for i in range(n+1):#row
    for j in range(i):#col
        print(num,end=' ')#1,space
        num=num+1#1=1+1=2
    print()    
