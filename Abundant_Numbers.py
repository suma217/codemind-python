def is_abundant(n):
    fac_sum=sum([fac for fac in range(1,n)if n%fac==0])
    return fac_sum>n
a=int(input())
if is_abundant(a):
    print(True)
else:
    print(False)