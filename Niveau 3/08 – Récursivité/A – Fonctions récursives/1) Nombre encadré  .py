def encadreNombre(nombre, nbCrochets):
   if nbCrochets == 0:
      print(nombre, end = "")
      return
   print("[", end = "")
   encadreNombre(nombre, nbCrochets - 1)
   print("]", end = "")
nombre, nbCrochets = map(int, input().split())
encadreNombre(nombre, nbCrochets)