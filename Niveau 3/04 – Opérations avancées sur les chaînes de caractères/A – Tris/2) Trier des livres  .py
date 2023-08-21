a=int(input())
liste=[""]*a
for i in range(a):
    liste[i]=input()
liste.sort()
for i in liste:
    print(i)