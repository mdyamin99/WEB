n=int(input())
tmp=int(n)
rev=0
while n:
    rev=rev*10+n%10
    n=n//10
if tmp==rev:
    print(rev)
    print("YES")
else:
    print(rev)
    print("NO")