liste=[]
for i in range(int(input())) :
    nb,date=map(int,input().split())
    if nb<0 :
        liste=liste[-nb:]
    else :
        liste+=[date for i in range(nb)]
print(min(liste))