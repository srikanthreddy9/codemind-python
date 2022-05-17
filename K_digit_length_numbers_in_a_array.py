n,k=map(int,input().split())
l=list(map(int,input().split()))
d=0
for i in range(0,n):
    c=l[i]
    if c<0:
        b=str(c)
        x=b[1:]
        c=int(x)
    f=len(list(str(c)))
    if k==f:
        d+=1
print(d)