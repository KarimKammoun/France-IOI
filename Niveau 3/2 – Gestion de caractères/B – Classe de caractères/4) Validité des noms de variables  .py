a=int(input())
for i in range(a):
    b=input()
    s=0
    if "A"<=b[0].upper()<="Z" or b[0]=="_":
        for i in range(1,len(b)):
            if "A"<=b[i].upper()<="Z" or b[i]=="_" or "0"<=b[i]<="9":
                s=s+1
    if s==len(b)-1:
        print("YES")
    else:
        print("NO")