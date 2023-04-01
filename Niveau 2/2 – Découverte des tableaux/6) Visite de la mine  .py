a=int(input())
liste=[0]*a
for i in range(a):
    liste[i]=int(input())
for i in range(a):
    if liste[-(i+1)]==1: print("2")
    if liste[-(i+1)]==2: print("1")
    if liste[-(i+1)]==3: print("3")
    if liste[-(i+1)]==4: print("5")
    if liste[-(i+1)]==5: print("4")