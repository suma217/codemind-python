n=int(input())
l=list(map(int,input().split()))
os=0
for i in range(n):
    if i%2!=0:
        os+=l[i]
print(os)