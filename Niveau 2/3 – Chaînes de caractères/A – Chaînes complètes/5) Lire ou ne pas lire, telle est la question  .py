a=int(input())
liste=[0]*a
b=0
for i in range(a):
    c=input()
    if b<len(c):
        liste[i]=c
        b=len(c)
for i in range(a):
    if liste[i]!=0:
        print(liste[i])