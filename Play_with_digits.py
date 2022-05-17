n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    a=l[i]
    d=str(a)
    e=map(int,d)
    f=list(e)
    c=c+sum(f)
print(c)