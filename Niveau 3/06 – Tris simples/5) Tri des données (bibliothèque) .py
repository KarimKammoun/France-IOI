a=int(input())
liste=list(map(int, input().split()))
liste.sort()
for i in range(a):
    if i==a-1:
        print(str(liste[i]))
        break
    print(str(liste[i]),end=" ")