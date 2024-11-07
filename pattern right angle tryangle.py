#pattern (right angle triangle)
n=int(input("enter n value"))
for i in range(1,n+1):
    print("*" *i) 

#pattern (right angle triangle reverse
n=int(input("enter n value"))
for i in range(n,0,-1):
    print("*" *i,end="\n") 
