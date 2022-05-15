n=int(input())
l=list(map(int,input().split()))
d=0
for i in range(n):
        c=0
        for j in range(1,l[i]+1):
            if l[i]%j==0:
                c+=1
        if c==2:
            d+=1
print(d)