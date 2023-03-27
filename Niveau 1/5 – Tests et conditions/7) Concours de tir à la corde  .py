a=int(input())
b=c=0
for i in range (a):
    b=b+int(input())
    c=c+int(input())
if b>c:
    print("L'équipe 1 a un avantage")
    print("Poids total pour l'équipe 1 :",b)
    print("Poids total pour l'équipe 2 :",c)
else:
    print("L'équipe 2 a un avantage")
    print("Poids total pour l'équipe 1 :",b)
    print("Poids total pour l'équipe 2 :",c)