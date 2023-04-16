a,b=map(int, input().split(" "))
liste=input().split(" ")
liste1=list(map(int,liste))
liste1.sort()
liste2=(liste1[a-b:a+1])
c=""
for i in range(b):
    c=c+str(liste2[-(i+1)])+" "
print(c)