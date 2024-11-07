a=float(input("enter a value :"))
b=float(input("enter b value :"))
c=input("select from +,-,/,%,*,// : ")
if(c== "+"):
    print("addtion",a+b)
elif(c== "-"):
    print("sub",a-b)
elif(c== "*"):
    print("multiple",a*b)
elif(c == "/"):
    if (b!=0):
      print("division",a/b)
    else:
      print("division not processed")
elif(c == "%"):
    print("modulo",a%b)
else:
    print("invalid")
       