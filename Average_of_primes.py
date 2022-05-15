n=int(input())
l=list(map(int,input().split()))
s=0
f=[]
c=0
for i in range(n):
    d=0
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            d+=1
    if d==2:
        s=s+l[i]
        c+=1
r=s/c
print('%.2f'%r)