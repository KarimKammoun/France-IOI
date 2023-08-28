def écrire_base(n: int, base: int) -> None:
    """Écrit l'entier 'n', dans la 'base'.

    >>> écrire_base(1234, 100)
    2
    12 34
    
    """
    chiffres = []
    while n > 0:
        chiffre = n % base
        n = n // base
        chiffres.append(chiffre)

    if chiffres == []:
        print(1) # un seul chiffre
        print(0) # le chiffre 0
    else:
        print(len(chiffres))
        for chiffre in chiffres[::-1]:
            print(chiffre, end=" ")
        print()

n, base = map(int, input().split())
écrire_base(n, base)