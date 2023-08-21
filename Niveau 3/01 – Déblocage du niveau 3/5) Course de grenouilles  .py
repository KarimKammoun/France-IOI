nb=int(input())
liste=[0]*nb
liste1=[0]*nb
nbtours=int(input())
for i in range(nbtours) :
    if liste.count(max(liste)) ==1 :
        liste1[liste.index(max(liste))]+=1
    num,d=map(int,input().split(" "))
    liste[num-1]+=d
print(liste1.index(max(liste1))+1)