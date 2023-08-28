def lire_base(chiffres: list, base: int) -> int:
    """Renvoie la valeur du nombre, avec ses 'chiffres' donnés en 'base'.

    >>> lire_base([3, 11], 12)
    47

    """
    résultat = 0
    for chiffre in chiffres:
        résultat *= base
        résultat += chiffre
    return résultat

def écrire_base(n: int, base: int) -> None:
    """Écrit l'entier 'n', dans la 'base'.

    >>> écrire_base(1234, 100)
    12 34

    """
    chiffres = []
    while n > 0:
        chiffre = n % base
        n = n // base
        chiffres.append(chiffre)

    if chiffres == []:
        print(0) # le chiffre 0
    else:
        for chiffre in chiffres[::-1]:
            print(chiffre, end=" ")
        print()

b1, b2, c = map(int, input().split())
chiffres = map(int, input().split())
écrire_base(lire_base(chiffres, b1), b2)