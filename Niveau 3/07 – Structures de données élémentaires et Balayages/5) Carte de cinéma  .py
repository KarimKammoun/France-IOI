n=int(input())
liste=[int(i) for i in input().split()]
liste.sort()
liste_1=[]
for i in range(1,n) :
    if liste[i]==liste[i-1] :
        liste_1.append(liste[i])
print(max(liste_1) if len(liste_1)>0  else  "-1")