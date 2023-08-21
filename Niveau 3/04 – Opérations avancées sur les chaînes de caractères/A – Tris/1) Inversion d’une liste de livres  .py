a=int(input())
liste=[""]*a
for i in range(a):
    liste[-(i+1)]=input()
for i in liste:
      print(i)