n=int(input())
l=list(map(int,input().split()))
a=0
s=0
for i in l:
    a+=i
s=a//n
print(s in l)