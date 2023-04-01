def min2(a,b):
    if a<b:
        return a
    elif b<a:
        return b
    else:
        return a
a=min2(int(input()),int(input()))
for i in range(8):
    b=min2(a,int(input()))
    if b<a:
        a=b
print(b)