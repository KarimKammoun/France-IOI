def calcul(a):
    b=0
    for i in range(len(a)):
        b=b+(ord(a[i])-65)
    c=str(b)
    while True:
        d=0
        if int(c)<10:
            break
        else:
            for i in range(len(c)):
                d=d+int(c[i])
            c=str(d)
    return c
a,b=input().split(" ")
c=calcul(a)
d=calcul(b)
print(c," ",d)