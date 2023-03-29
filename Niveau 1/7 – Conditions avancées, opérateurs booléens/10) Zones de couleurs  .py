a=int(input())
liste=[0]*(a*2)
for i in range (a*2):
    liste[i]=int(input())
for i in range (0,a*2,2):
    if 25<liste[i]<50 and 20<liste[i+1]<45:
      print("Dans une zone jaune")
    elif 10<liste[i]<85 and 10<liste[i+1]<55:
        print("Dans une zone bleue")
    elif 15<liste[i]<45 and 60<liste[i+1]<70:
        print("Dans une zone rouge")
    elif 60<liste[i]<85 and 60<liste[i+1]<70:
        print("Dans une zone rouge")
    elif 0<liste[i]<90 and 0<liste[i+1]<70:
        print("Dans une zone jaune")
    else:
        print("En dehors de la feuille")