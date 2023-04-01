a=int(input())
liste=[0]*a
for i in range(a):
    liste[i]=int(input())
liste.sort()
for i in range(a//2):
    print("{} {}".format(liste[i],liste[-(i+1)]))
    



