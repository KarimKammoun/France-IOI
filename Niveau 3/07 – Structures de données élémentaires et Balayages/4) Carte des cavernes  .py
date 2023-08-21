n=int(input())
liste=[c for c in input().replace(" ", "")]
liste_1=[]
for c in liste :
    if len(liste_1)>0 :
        if c!=liste_1[-1] and c!="(":
            del liste_1[-1]
            continue
    liste_1.append(c)
print("1" if len(liste_1)==0 else "0")