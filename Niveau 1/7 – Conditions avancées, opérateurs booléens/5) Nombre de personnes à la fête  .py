a=int(input())
b=0
c=0
for i in range(a*2):
    if int(input())>0:
        b=b+1
    else:
        b=b-1
    if b>c:
        c=b
print(c)

    