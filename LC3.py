n1=int(input("Enter first num= "))
n2=int(input("Enter second num= "))
n3=int(input("Enter third num= "))
if(n1>n2 and n1>n3):
    print(n1," is greater")
elif(n2>n1 and n2>n3):
    print(n2," is greater")
else:
    print(n3," is greater")
