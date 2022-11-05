n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in l:
    if i%2==1:
        a+=1
for i in range(n):
    if i%2==1 and l[i]%2==1:
        b+=1
print(b==a)