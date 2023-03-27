a=int(input())
b=0
d=0
for i in range(a):
   c=int(input())
   if c>0:
      b=b+c
   if c<0:
      d=d+abs(c)
print(b)
print(d)