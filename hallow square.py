m= int(input("enter m value"))
n = int(input("enter n value"))
for i in range(m) :
    if i==0 :
        print("* " * n)
    elif i == (m-1) :
        print("* " * n)
    else:
        space = (n-2) * "  "
        print("* " + space + "* ")   


#another method (without elif condition)
n = int(input("enter n value"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()                
