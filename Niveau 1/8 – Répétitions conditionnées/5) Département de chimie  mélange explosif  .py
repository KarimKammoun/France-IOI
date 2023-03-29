a=int(input())
b=int(input())
c=int(input())
d=0
e=True
while d<a and e:
   f=int(input())
   e=(b<=f and f<=c)
   if e:
      print("Rien à signaler")
   else:
      print("Alerte !!")
   d=d+1