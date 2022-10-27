t=int(input())
for i in range(t):
    n=int(input())
    l=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if l==rev:
        print(True)
    else:
        print(False)