n=int(input())
a=0
b=1
print(a,b,end=' ')
while n>2:
    a,b=b,a+b
    print(b,end=' ')
    n-=1
    