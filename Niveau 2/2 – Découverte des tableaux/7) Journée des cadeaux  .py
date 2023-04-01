a=int(input())
liste=[0]*a
for i in range(a):
    liste[i]=int(input())
liste.sort()
if a%2==0:
    print(((liste[a//2])+(liste[(a//2)-1]))/2)
else:
    print(liste[a//2])