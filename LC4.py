op=input("Enter operator= ")
n1=int(input("Enter num1= "))
n2=int(input("Enter num2= "))
if(op=="+"):
    print("Sum = ",n1+n2)
elif(op=="-"):
    print("Difference= ",n1-n2)
elif(op=="/"):
    print("Quotient= ",n1/n2)
else:
    print("Product= ",n1*n2)