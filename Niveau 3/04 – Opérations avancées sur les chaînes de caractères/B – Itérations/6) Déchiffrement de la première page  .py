a=input()
b=input()
c=""
for i in range(len(b)):
    if "a"<=b[i]<="z":
        d=ord(b[i])-97
        c=c+(a[d].lower())
    elif "A"<=b[i]<="Z":
        d=ord(b[i])-65
        c=c+(a[d].upper())
    else:
        c=c+b[i]
print(c)