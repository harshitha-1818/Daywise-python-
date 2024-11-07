a=int(input("enter a value :"))
b=int(input("enter b value :"))
c=int(input("enter c value :"))
if(a+b>c and b+c>a and c+a>b):
    if a== b== c:
        print("the triangle is equilateral")
    elif(a==b or b==c or a==c):
        print("the triangle is isosceles")
    else:
        print("the triangle is scalene ")
else:
    print("the lengths do not form a valid triangle")        



