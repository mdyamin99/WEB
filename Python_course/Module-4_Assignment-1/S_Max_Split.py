s=input()
ch=''
cnt=0
bl=0
ans=[]
for c in s:
    ch+=c
    if c=='R':
        bl+=1
    else:
        bl-=1
    if bl==0:
        ans.append(ch)
        cnt+=1
        ch=''
print(cnt)
for c in ans:
    print(c)