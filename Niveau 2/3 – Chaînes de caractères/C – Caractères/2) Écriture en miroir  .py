a=int(input())
liste=[0]*a
for i in range(a):
    b=input()
    c=b[::-1]
    liste[i]=c
for i in range(a):
    print(liste[i])