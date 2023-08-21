n=int(input())
liste=[int(i) for i in input().split()]
liste_1=liste.copy()
liste_1.sort()
liste_index=[]
while liste!=liste_1 :
    for i in range(len(liste)-1) :
        if liste[i]>liste[i+1] :
            liste[i],liste[i+1]=liste[i+1],liste[i]
            liste_index.append(str(liste[i+1])+" "+str(liste[i]))
        
    
print(len(liste_index))
print("\n".join(liste_index))