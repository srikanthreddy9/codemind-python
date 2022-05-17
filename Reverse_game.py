n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    s=str(l[i])
    d=int(s[::-1])
    print(d,end=" ")
  