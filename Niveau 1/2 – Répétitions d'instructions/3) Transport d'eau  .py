a=int(input())
lon_max=int(input())
lar_max=int(input())
lon_min=lon_max
lar_min=lar_max
for i in range(a-1):
   b=int(input())
   c=int(input())
   if b>lon_max:
       lon_max=b
   if b<lon_min:
       lon_min=b
   if c>lar_max:
       lar_max=c
   if c<lar_min:
       lar_min=c
   print(lon_min,lar_min)
d=lon_max-lon_min
e=lar_max-lar_min
print((d*2)+(e*2))
