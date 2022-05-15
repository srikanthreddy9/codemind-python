n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    if i %2==0:
        a=l[i]
        for j in range(l[i+1]):
            print(a,end=' ')