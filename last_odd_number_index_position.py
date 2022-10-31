n=int(input())
l=list(map(int,input().split()))
os=0
for i in range(n):
    if l[i]%2!=0:
        os=i
print(os)