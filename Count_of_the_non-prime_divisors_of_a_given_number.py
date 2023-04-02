def prime(x):
    f=0
    for i in range(1,x+1):
        if x%i==0:
            f+=1
    if f==2:
        return True
    else:
        return False
x=int(input())
c=0
for i in range(1,x+1):
    if x%i==0:
        if prime(i)!=True:
            c+=1
print(c)