a, b = map(int, input().split())
c = []
for i in range(a):
    liste = input().split()
    for j in liste:
        c.append(len(j))
c.sort()
d = 1
for i in range(len(c)-1):
    if c[i] == c[i+1]:
        d = d + 1
    else:
        print(c[i], ":", d)
        d = 1
print(c[-1], ":", d)

