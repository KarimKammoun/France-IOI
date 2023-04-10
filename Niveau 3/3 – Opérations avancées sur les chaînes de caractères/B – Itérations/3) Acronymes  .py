def change (a,f):
    b=(a.lower())+"  "
    c=""
    d=0
    e=0
    g=0
    for i in range(len(b)-1):
        if b[i]==" " :
            g=g+1
            if e==len(f):
                break
            if b[d] != " " :
                if b[d].upper() != f[e]:
                    break
            c=c+(b[d].upper()+b[(d+1):i+1])
            d=i+1
            e=e+1
    c=c[0:len(c)-1]
    return [c,g]
liste=[]
a=input()
b=int(input())
for i in range(b):
    c=input()
    d=change(c,a)
    if len(d[0])==len(c) and d[1]==len(a):
        liste.append(d[0])
for i in range(len(liste)):
    print(liste[i])