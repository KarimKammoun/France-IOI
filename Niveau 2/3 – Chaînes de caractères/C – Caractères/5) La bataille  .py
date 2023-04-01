a = input()
b = input()
c = 0
while c<len(a) and c<len(b) and a[c]==b[c]:
   c=c+1
if c==len(a) and c==len(b):
   print("=")
elif c==len(b) or (c<len(a) and a[c]<b[c]):
   print(1)
else:
   print(2)
print(c)