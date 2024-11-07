#pyramid
n=int(input("enter n value:"))
for i in range(n):
    print(' '*(n - i - 1) + '*' * (2 *i + 1))

#pyramid using nestend loop
n=int(input("enter n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*', end=" ")
    print()   

#reverse pyramid
n=int(input("enter n value:"))
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print('*', end=" ")
    print()   

