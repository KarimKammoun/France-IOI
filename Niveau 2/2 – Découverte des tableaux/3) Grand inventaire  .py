a= int(input())
liste=[0]*10
for i in range(a):
    b=int(input())
    liste[b-1]=liste[b-1]+int(input())
for i in liste:
    print(i)


