n=int(input())
f=0
s=1
for i in range(0,n):
    if (i<=1):
        count=i
    else:
        count=f+s
        f=s
        s=count
    print(count,end=' ')