a=input()
a=a.upper()
liste=[0]*27
for i in range(len(a)):
    if a[i]!= " ": 
        liste[(ord(a[i]))-65]=liste[(ord(a[i]))-65]+1
b=0
c=0
for i in range(27):
    if liste[i]>b:
        c=i
        b=liste[i]
print(chr(c+65))


