from robot import *
haut()
for i in range(10):
    for j in range(8):
        if i%2==0:
            haut()
            if j==7:
                droite()       
        else:
            bas()
            if j==7 and i != 9:
                droite()
bas()
for i in range(9):
    gauche()