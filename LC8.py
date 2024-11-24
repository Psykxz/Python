"""number of digits"""

n=int(input("Enter a number: "))
t=n
count=0
while(t>0):
    t=t//10
    count+=1
print("Number of digits in ",n," is ",count )


