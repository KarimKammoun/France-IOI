a=input()
b=0
liste=[0]*26
for i in range(len(a)):
    if "A"<=a[i].upper()<="Z":
        b=b+1
    if 0<=((ord(a[i].upper()))-65)<26:
        liste[((ord(a[i].upper()))-65)]=liste[((ord(a[i].upper()))-65)]+1
for i in range(26):
    print((liste[i])/b)