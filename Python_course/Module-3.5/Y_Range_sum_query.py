n,q=map(int,input().split())
numbers=list(map(int,input().split()))
pre=[0]*(n)
pre[0]=int(numbers[0])
for i in range(1,n):
    pre[i]=int(pre[i-1]+numbers[i])

for i in range(q):
    l,r=map(int,input().split())
    l-=1
    r-=1
    sum=0
    if l==0:
        sum=pre[r]
    else:
        sum=pre[r]-pre[l-1]
    print(sum)