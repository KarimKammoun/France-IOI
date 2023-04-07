nl,nj =map(int,input().split(" "))
liste=[1]*nl
c=""
for i in range(nj):
    nc=int(input())
    for i in range(nl):
        if liste[i]!=0:
            liste[i]=liste[i]-1
    for j in range(nc):
        niml,nimj=map(int,input().split(" "))
        if liste[niml]==0:
            liste[niml]=nimj
            c=c+"1"
        else:
            c=c+"0"
for i in range(len(c)):
    print(c[i])