a=int(input())
b=[0.0]*a
c=0.0
for i in range(a):
   b[i]=float(input())
   c=c+b[i]
d=c/a
for i in range(a):
   print(d-b[i])
