from sys import stdin
 
def lireEtInverser():
   caractere = stdin.read(1)
   if caractere != "\n":
      lireEtInverser()
      print(caractere,end="")
 
lireEtInverser()