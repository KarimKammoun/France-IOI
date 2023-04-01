a=int(input())
b=int(input())
liste=[]
for i in range(a):
    t=input()
    c=input()
    if len(c)<b:
        liste.append(t)
for i in range(len(liste)):
    print(liste[i])