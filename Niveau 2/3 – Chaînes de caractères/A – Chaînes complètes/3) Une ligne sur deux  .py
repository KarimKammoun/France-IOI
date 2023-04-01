a=int(input())
liste=[0]*a
for i in range(a):
    liste[i]=input()
for i in range (a):
    if (i%2)== 0:
        print(liste[i])