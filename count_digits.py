n=int(input())
l=list(map(int,input().split()))
d=0
for i in range(0,n):
    c=l[i]
    if c<0:
        b=str(c)
        x=b[1:]
        c=int(x)
    f=len(list(str(c)))
    print(f,end=" ")