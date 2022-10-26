a,b,c=map(int,input().split())
s=(a+b+c)/2
l=s*(s-a)*(s-b)*(s-c)
area=(l)**(1/2)
print('{:.2f}'.format(area))