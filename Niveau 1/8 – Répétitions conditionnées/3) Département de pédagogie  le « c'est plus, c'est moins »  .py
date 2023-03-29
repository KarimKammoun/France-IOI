a=int(input())
b=True
i=1


while b==True:
    c=int(input())
    if c<a:
        print("c'est plus")
        i=i+1
    elif c>a:
        print("c'est moins")
        i=i+1
    else:
        print("Nombre d'essais nécessaires :")
        print(i)
        b=False