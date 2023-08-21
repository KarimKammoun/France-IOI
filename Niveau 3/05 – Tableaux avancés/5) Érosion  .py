import sys
def main():
   nbPassages = int(sys.stdin.readline())
   nbLignes, nbColonnes = map( int, sys.stdin.readline().split() )
   grille = [list(sys.stdin.readline()) for loop in range(nbLignes)]
   grille = [grille,[[0]*nbColonnes for loop in range(nbLignes)]]
    
   source = 0
   for loop in range(nbPassages):
      destination = 1 - source
      for ligne in range(nbLignes):
         for colonne in range(nbColonnes):
            if grille[source][ligne][colonne] == '.' or\
                  (ligne == 0) or (ligne == nbLignes-1) or\
                  (colonne == 0) or (colonne == nbColonnes-1) or\
                  (grille[source][ligne-1][colonne] == '.') or\
                  (grille[source][ligne+1][colonne] == '.') or\
                  (grille[source][ligne][colonne-1] == '.') or\
                  (grille[source][ligne][colonne+1] == '.'):
               grille[destination][ligne][colonne] = '.'
            else:
               grille[destination][ligne][colonne] = '#'
      source = destination
 
   for ligne in grille[source]:
      print("".join(ligne))
       
main()
