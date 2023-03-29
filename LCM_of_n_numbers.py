def LCM(x,y):
    if y>x:
        for i in range(1,y+1):
            if (y*i)%x==0:
                return y*i
    else:
        for i in range(1,x+1):
            if (x*i)%y==0:
                return x*i
n=int(input())
arr=list(map(int,input().split()))
lcm=1
for i in range(n):
    lcm=LCM(lcm,arr[i])
print(lcm)