def gomoku(n,grille) :
    vecteurs=[(1,0),(0,1),(1,1),(1,-1)]
    def est_valider(i,j) :
        return (0<=i<n)and(0<=j<n)
    def verifier (i,j,di,dj) :
        joueur =grille [i][j]
        for k in range(1,5) :
            i+=di ; j+=dj
            if (not est_valider(i,j)) or joueur!=grille[i][j] :
                return 0
        return joueur
    for i in range(n) :
        for j in range(n) :
            if grille [i][j]!=0 :
                for di,dj in vecteurs :
                    joueur=verifier(i,j,di,dj)
                    if joueur !=0 :
                        return joueur
    return 0
n=int(input())
grille=[list(map(int,input().split())) for i in range(n)]
print(gomoku(n,grille))

