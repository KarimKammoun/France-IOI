def cardinalIntersectionTableauxTries(valeursA, valeursB):
   nbIntersectent = 0
   posA = 0
   posB = 0
   while posA < len(valeursA) and posB < len(valeursB):
      valeurA = valeursA[posA]
      valeurB = valeursB[posB]
      if valeurA < valeurB:
         posA += 1
      elif valeurA > valeurB:
         posB += 1
      else:
         posA += 1
         posB += 1
         nbIntersectent += 1
   return nbIntersectent
   
 
def main():
   _ = int(input())
   valeursA = list(map(int, input().split()))
   _ = int(input())
   valeursB = list(map(int, input().split()))
   valeursA.sort()
   valeursB.sort() 
 
   print(cardinalIntersectionTableauxTries(valeursA, valeursB))
   
main()