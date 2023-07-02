n=int(input())
liste=[]
for i in range(n)  :
    liste.append([int(c) for c in input().split()[::-1] ])
liste.sort()
for c in liste :
    print(c[1],c[0])