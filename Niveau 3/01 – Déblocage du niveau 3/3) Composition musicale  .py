def convertir(a):
    for i in range((len(a))-1):
        if a[i]==a[i+1]:
            c=a[0:i]+a[(i+2):len(a)]
            return c
    return a
a=input()
b=convertir(a)
while True:
    if b==a:
        print(b)
        break
    else:
        a=b
        b=convertir(a)