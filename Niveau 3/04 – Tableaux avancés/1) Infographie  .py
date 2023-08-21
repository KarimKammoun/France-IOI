a,b=map(int,input().split(" "))
liste=[["."]*b for i in range(a)]
for i in range(int(input())): 
    iLig1,iCol1,iLig2,iCol2,ch=input().split(" ")
    for j in range(int(iLig1),int(iLig2)+1) :
        for n in range(int(iCol1),int(iCol2)+1) :
            liste[j][n] =ch
for i in liste :
    print(''.join(i))
