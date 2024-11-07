a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if(a>c and a>b):
    print(a,"a is greater")
elif(b>a and b>c):
    print(b,"b is greater")
#elif(c>a and c>b):
 #   print(c,"c is greater")
#elif(a==b or a==c):
 #   print("both are equal")
else:
    print(c,"c is greater")