NB_PILES = 2
INFINI = 1000*1000*1000
piles = []
nbValeurs = 0
for pile in range(NB_PILES):
   nbValeurs += int(input())
   valeurs = map(int,input().split())
   pile = [INFINI]
   pile.extend(reversed(list(valeurs)))
   piles.append( pile )
while nbValeurs > 0:
   iPileMin = 0
   if piles[0][-1] > piles[1][-1]:
      iPileMin = 1
   print(piles[iPileMin].pop(),end=" ")
   nbValeurs -= 1