a=int(input())
liste=set(map(int,input().split()))
b=int(input())
for i in range(b):
    c=int(input())
    if c in liste:
        print(1)
    else:
        print(0)
