a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=""
for i in range(a):
    e=e+"X"
print(e)
print()
for i in range(b):
    f=""
    if i==0 or i==(b-1):
        for j in range(c):
            f=f+"#"
        print(f)
    else:
        for j in range(c):
            if j==0 or j==(c-1):
                f=f+"#"
            else:
                f=f+" "
        print(f)
print()
for i in range(d):
    g=""
    if i==0:
        print("@")
    elif i==(d-1):
        for j in range(d):
            g=g+"@"
        print(g)
    else:
        for j in range(i+1):
            if j==0 or j==(i):
                g=g+"@"
            else:
                g=g+" "
        print(g)