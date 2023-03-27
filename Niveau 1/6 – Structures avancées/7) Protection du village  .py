nbMaisons = int(input())
xMin = 1000 * 1000
xMax = 0
yMin = 1000 * 1000
yMax = 0
for loop in range(nbMaisons):
   posX = int(input())
   posY = int(input())
   if posX < xMin:
      xMin = posX
   if posX > xMax:
      xMax = posX
   if posY < yMin:
      yMin = posY     
   if posY > yMax:
      yMax = posY
largeur = xMax - xMin
hauteur = yMax - yMin
perimetre = 2 * (largeur + hauteur)
print(perimetre)