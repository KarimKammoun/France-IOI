a=int(input())
b="a"*((a*2)-1)
d=len(b)
print(b)
for i in range(a):
    if i ==0:
        continue
    c=""
    for j in range((((a*2)-1)-(i*2))):
        c=c+chr(i+97)
    b=b[0:i]+c+b[d-i:d]
    print(b)
for i in range(a-2,-1,-1):
    c=""
    for j in range((((a*2)-1)-(i*2))):
        c=c+chr(i+97)
    b=b[0:i]+c+b[d-i:d]
    print(b)