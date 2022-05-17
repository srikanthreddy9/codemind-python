n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    s=str(l[i])
    d=s[::-1]
    if s==d:
        c+=1
#print(n,k,l)
print(c)