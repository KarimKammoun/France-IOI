a=int(input())
liste=[""]*a
for i in range(a):
    b=input()
    b=b[(b.find(" "))+1::]+" "+b[0:(b.find(" "))+1]
    liste[i]=b
liste.sort()
for i in liste:
    print(i)