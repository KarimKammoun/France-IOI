def afficheNombresEntre(debut, fin):
   print(debut, end = "");
   if debut == fin:
      print()
   else:
      print(" ", end = "")
      afficheNombresEntre(debut + 1, fin)
  
debut, fin = map(int, input().split())
afficheNombresEntre(debut, fin)
