a=int(input())
liste=[0]*a

for i in range(a):
    liste[i]=input()
for i in range(a):
    b=liste[i]
    c=b[-1]
    if c=="g":
        print(str(round((float(b[0:-2])*0.002205),6))+" l")
    elif c=="m":
        print(str(round(((float(b[0:-2]))/0.3048),6))+" p")
    else:
        print(str(round(((float(b[0:-2])*1.8)+32),6))+" f")