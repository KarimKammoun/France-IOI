a=int(input())
liste=[0]*2
liste2=[0]*a
liste3=[]*a
for i in range(a):
    b=list(map(int,input().split()))
    liste.append(sum(b))
    liste3+=b
    liste[0]+=b[i]
    liste[1]+=b[-(i+1)]
    for j in range(a):
        liste2[j]+=b[j]
s=liste+liste2
d=s[0]
liste3.sort()
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        p="no"
        break
    if i==(len(s)-1):
        p="yes"
for i in range(1,(a*a)+1):
    if liste3[i-1]!=i:
        p="no"
print(p)
