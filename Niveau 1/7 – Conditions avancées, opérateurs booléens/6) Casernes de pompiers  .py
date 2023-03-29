a=int(input())
for i in range (a):
    liste=[0]*8
    for i in range (8):
        liste[i]=int(input())
    if not(liste[1]<=liste[4] or liste[5]<=liste[0])and not(liste[3]<=liste[6] or liste[7]<=liste[2]):
        print("OUI")
    else:
        print("NON")