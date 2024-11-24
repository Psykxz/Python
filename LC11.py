s=input("Enter a string: ")
n=len(s)
l=[]
l=list(s)
l[0],l[n-1]=l[n-1],l[0]
for i in l:
    print(i,end=" ")