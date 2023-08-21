a=int(input())
liste=[""]*a
for i in range(a):
    liste[i]=input()
b=""
for i in liste:
    if i>b:
        print(i)
        b=i