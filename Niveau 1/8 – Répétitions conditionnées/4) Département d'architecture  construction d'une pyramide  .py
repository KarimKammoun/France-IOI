a=int(input())
b=0
h=1
while b+h*h <= a:
   b=b+h*h
   h=h+1  
print(h-1)
print(b)