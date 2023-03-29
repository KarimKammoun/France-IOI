a=int(input())
for i in range(a):
    s=0
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    f=int(input())
    if 182>=b>=178:
        s=s+1
    if c>=34:
        s=s+1
    if d<70:
        s=s+1
    if e==0:
        s=s+1
    if f==1:
        s=s+1
    if s==5:
        print("Très probable")
    elif s==3 or s==4:
        print("Probable")
    elif s==0:
        print("Impossible")
    else:print("Peu probable")
