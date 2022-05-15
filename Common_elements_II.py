n,m=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
e=[]
f=[]
c=0
for i in range(n):
    if l[i] not in e:
        e.append(l[i])
for j in range(m):
    if s[j] not in f:
        f.append(s[j])
for k in range(len(e)):
    if e[k] not in f:
        print(e[k],end=' ')
for g in range(len(f)):
    if f[g] not in e:
        print(f[g],end=' ')