n=int(input())
l=list(map(int,input().split()))
es=0
for i in range(n):
    if i%2==0:
        es+=l[i]
print(es)