import sys
def main():
   nbRequêtes = int(input())
   nbAffiches = 0
   affiches = [0]*nbRequêtes
   for requête,_ in zip( sys.stdin, range(nbRequêtes) ):
      requête = requête.split()
      if requête[0] == 'Q':
         print(nbAffiches)
      else:
         affiche = int(requête[1])
         while (nbAffiches > 0) and (affiches[nbAffiches-1] <= affiche):
            nbAffiches -= 1
         affiches[nbAffiches] = affiche
         nbAffiches += 1
      
main()