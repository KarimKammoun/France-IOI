a=int(input())
b=int(input())
liste=[0]*a
for i in range(a):
    liste[i]=int(input())
for i in range(b):
    c=int(input())
    d=int(input())
    if c==d:
        continue
    liste[c]=liste[c]+liste[d]
    liste[d]=liste[c]-liste[d]
    liste[c]=liste[c]-liste[d]
for i in range(a):
    print(liste[i])
    