a=input()
b=int(input())
c=""
d=0
for i in range(b):
    c=c+input()+" "
for i in range(len(c)):
    if c[i]==a:
        d=d+1
print(d)