n=int(input())
l=list(map(int,input().split()))
a=0
q=0
for i in l:
    a+=i
q=a/n
print('%.2f'%q)