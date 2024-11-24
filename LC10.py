import math

a=int(input("enter coeff of x^2: "))
b=int(input("enter coeff of x: "))
c=int(input("enter constant c: "))

d=(b*b)-(4*a*c)
x=(-b+math.sqrt(d))/(2*a)
y=(-b-math.sqrt(d))/(2*a)
#print(d,x,y)
if d>0:
    print("two real and distinct roots\nThey are: ",x,y)
elif d==0:
    print("one real root\nthey are: ",x,y)
else:
    print("no real roots")

