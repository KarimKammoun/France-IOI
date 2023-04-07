a=int(input())
for i in range(a):
    b=input()
    c=""
    for i in range(len(b)):
        if b[i]!=" ":
            c=c+b[i]
    d=c.upper()
    if d==d[::-1]:
        print(b)
