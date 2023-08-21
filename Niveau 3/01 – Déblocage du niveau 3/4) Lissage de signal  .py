def verif (liste):
    d=0
    lis=liste.copy()
    for i in range(1,len(liste)-1):
        liste[i]=(lis[i-1]+lis[i+1])/2
        if abs(liste[i-1]-liste[i])<b :
            d=d+1
    if (abs(liste[-1]-liste[-2]))<b :
            d=d+1
    if d==(len(liste))-1:
       return True
    else:
        return False
a=int(input())
b=float(input())
liste=[0]*a
for i in range(a):
    liste[i]=float(input())
c=0
while True:
    if len (liste)==2 or len (liste)==1 :
        print(0)
        break
    d=0
    for i in range(1,len(liste)-1):
        if abs(liste[i-1]-liste[i])<b :
            d=d+1
    if (abs(liste[-1]-liste[-2]))<b :
            d=d+1
    if d==(len(liste))-1:
        print(0)
        break
    if verif(liste)==True:
        print(c+1)
        break
    else:
        c=c+1