n=int(input())
liste=[int(c) for c in input().split()]
for i in range(int(input())) :
    liste_1=[int(i) for i in input().split()]
    liste[liste_1[0]-1]+=liste_1[1]
print(" ".join([str(i) for i in liste]))