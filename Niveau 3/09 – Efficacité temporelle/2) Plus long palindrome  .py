def main():
   texte = input()
   longueurTexte = len(texte)
   maximum = 1
   milieu = 1
   while milieu <= longueurTexte - maximum // 2:
      début = milieu - 1
      fin = milieu + 1
      while début >= 0 and fin < longueurTexte and texte[début] == texte[fin]:
         début -= 1
         fin += 1
      maximum = max(maximum, fin - début - 1)
      début = milieu - 1
      fin = milieu
      while début >= 0 and fin < longueurTexte and texte[début] == texte[fin]:
         début -= 1
         fin += 1
      maximum = max(maximum, fin - début - 1)
      milieu += 1
   print(maximum)
main()