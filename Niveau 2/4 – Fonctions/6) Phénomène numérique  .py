def calcule(a):
    b=a
    while True:
        if a==1:
            break
        if a%2==0:
            a=a//2
            print(a,end=" ")
        else:
            a=(a*3)+1
            print(a,end=" ")
calcule(a=int(input()))