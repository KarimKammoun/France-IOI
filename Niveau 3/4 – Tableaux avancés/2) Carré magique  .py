def cube(n,liste) :
    somme = sum(liste[0])
    if any(sum(ligne) != somme  for ligne in liste) : 
        return False
    if any (sum(liste[i][j] for i in range(n)) !=somme for j in range(n)):
        return False
    if sum(liste[i][i] for i in range(n)) != somme  : 
        return False                                        
    if sum(liste[i][-i-1] for i in range(n)) !=somme  :
        return False
    n_carré=n*n
    déja_vu=[False for i in range(n_carré)]
    for i in range(n) :
        for j in range(n) :
            if 0<liste[i][j]<=n_carré :
                if déja_vu[liste[i][j]-1] ==True :
                    return False
                déja_vu[liste[i][j]-1]=True
            else :
                return False
    return True
n=int(input())
liste=[list(map(int,input().split()))for i in range(n)]
print("yes" if cube(n,liste) else "no")