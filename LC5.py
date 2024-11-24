"""First n multiples"""

n=int(input("Enter a number: "))
y=int(input("Enter how many multiples u want: "))
multiples=[]
for i in range(1,y+1):
    multiples.append(n*i)
for i in multiples:
    print(i,end=" ")