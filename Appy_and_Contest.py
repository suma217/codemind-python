t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    c=n//a
    d=n//b
    if c>=k or d>=k:
        print('Win')
    else:
        print('Lose')