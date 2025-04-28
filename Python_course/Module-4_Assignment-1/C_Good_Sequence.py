n=int(input())
numbers=list(map(int,input().split()))
dictt={}
for num in numbers:
    if num in dictt:
        dictt[num]+=1
    else:
        dictt[num]=1
ans=0
for key,val in dictt.items():
    if key>val:
        ans+=val
    elif key<val:
        ans+=val-key
print(ans)