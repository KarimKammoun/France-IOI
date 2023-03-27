a=int(input())
c=0
d=0
for i in range (a):
    b=int(input())
    if i==0:
        c=b
    if b<=c:
        c=b
        d=i+1
print(d)