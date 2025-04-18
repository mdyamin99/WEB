s=list(input().split())
ans=[]
for c in s:
    ans.append(c[::-1])
print(*ans)