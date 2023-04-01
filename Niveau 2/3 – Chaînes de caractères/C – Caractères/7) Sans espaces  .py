liste=input().split(" ")
for i in range(len(liste)):
    if i==len(liste)-1:
        print(liste[i])
        break
    print(liste[i],end="_")
