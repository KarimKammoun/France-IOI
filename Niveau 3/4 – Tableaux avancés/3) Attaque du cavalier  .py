liste=[list(input().split())for i in range(8)]
liste.append(["000000000000"])
liste.append(["000000000000"])
liste.insert(0,["000000000000"])
liste.insert(0,["000000000000"])
for i in range(2,10):
    b=liste[i][0]
    liste[i][0]="00"+b+"00"
a=False
for i in range(2,10):
    for j in range(2,10):
        if liste[i][0][j]=="C":
            if "a"<=liste[i-2][0][j-1]<="z" or "a"<=liste[i-2][0][j+1]<="z" or "a"<=liste[i-1][0][j-2]<="z" or "a"<=liste[i-1][0][j+2]<="z" or "a"<=liste[i+2][0][j-1]<="z" or "a"<=liste[i+2][0][j+1]<="z" or "a"<=liste[i+1][0][j-2]<="z" or "a"<=liste[i+1][0][j+2]<="z":
                a=True
                break
    if a==True:
        break
if a==True:
    print("yes")
else:
    print("no")