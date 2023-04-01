a=input()
b=input()
for i in range(len(a)):
    if a[i]not in["A","E","I","O","U","Y"," "]:
        print(a[i],end="")
print()
for i in range(len(b)):
    if b[i]not in["A","E","I","O","U","Y"," "]:
        print(b[i],end="")
print()