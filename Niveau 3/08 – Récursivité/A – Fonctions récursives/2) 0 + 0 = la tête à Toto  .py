def teteAToto(niveau):
   if niveau == 0:
      print("0", end = "")
      return
   print("(", end = "")
   teteAToto(niveau - 1)
   print(" + ", end = "")
   teteAToto(niveau - 1)
   print(")", end = "")
  
niveau = int(input())
print("0 = ", end = "")
teteAToto(niveau)
print()