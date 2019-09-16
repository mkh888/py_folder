a=int(input())
i=1
count=1
for i in range(i,a):
    if(a%i==0):
        count=count+1    
if(count>2):
    print("yes")
else:
    print("no")
    
