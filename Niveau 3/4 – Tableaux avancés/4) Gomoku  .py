def calcule(liste,x,y,a,b):
    c=liste[x][y]
    if c==0:
        return 0
    d=0+a
    e=0+b
    for i in range(4):
        if c==liste[x+d][y+e]:
            d=d+a
            e=e+b
        else:
            return 0
    return c
a=int(input())
liste=[0]*a
for i in range(a):
    liste[i]=[0]*4+list(map(int,input().split(" ")))+[0]*4
for i in range(4):
    liste.append(([0]*(a+8)))
pos=[[1,0],[1,1],[0,1],[-1,1]]
for i in range(a):
    for j in range(4,a+4):
        for n in range(4):
            b=calcule(liste,i,j,pos[n][0],pos[n][1])
            if b==1:
                print(1)
                break
            elif b==2:
                print(2)
                break
            else:continue
        if b!=0:
            break
    if b!=0:
        break
if b==0:
    print(0)

