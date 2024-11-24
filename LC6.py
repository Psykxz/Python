import itertools
sum=0
count=0
for i in itertools.count(1):
    if(i%2==0):
        sum+=i
        count+=1
        if(count==100):
            break
print("Sum of first 100 even numbers is",sum)