a=int(input())
liste=[]
for i in range(a):
    b=input().split(" ")
    if int(b[0])>=0:  
        for i in range(int(b[0])):
            liste.append(b[1])
    else:
        liste=liste[0:(len(liste)+int(b[0]))]
print(min(liste))