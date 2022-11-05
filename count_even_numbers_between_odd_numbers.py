n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(n):
    if (i+2)<n and l[i]%2!=0 and l[(i+1)]%2==0 and l[(i+2)]%2!=0:
       a+=1
print(a)