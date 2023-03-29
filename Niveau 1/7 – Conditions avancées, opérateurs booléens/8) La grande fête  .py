a=int(input())
b=int(input())
c=int(input())
s=0
for i in range(c):
    d=int(input())
    e=int(input())
    if d<=b and e>=a or e>=a and d<=b:
        s=s+1
print(s)