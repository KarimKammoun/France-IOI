def cherche(liste,c,a):
    for i in range(a):
        if liste[i]>c and i !=0:
            return liste[i-1]
        if liste[i]>c and i==0:
            return liste[i]
        if liste[i]==c:
            return liste[i]
a=int(input())
liste=list(map(int,input().split(" ")))
liste.sort()
b=int(input())
for i in range(b):
    c=int(input())
    print(cherche(liste,c,a))