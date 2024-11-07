base=int(input("enter base value"))
exponent=int(input("enter a power value"))
print(base**exponent)

#another method without using ** and pow(with while)
base=int(input("enter base value"))
exponent=int(input("enter a power value"))
k=1
p=1
while k<=exponent:
    p=p*base
    k= k+1
print(p)


