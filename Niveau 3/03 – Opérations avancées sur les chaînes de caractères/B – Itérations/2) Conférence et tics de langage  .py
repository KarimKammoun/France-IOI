a=input()
s=0
liste=((input().upper())+" ").split(" ")
for i in liste:
    if a.upper()==i:
        s=s+1
print(s)