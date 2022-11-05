n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    if i%2==0:
        s+=1
for i in range(n):
    if i%2==0 and l[i]%2==0:
        c+=1
print(c==s)