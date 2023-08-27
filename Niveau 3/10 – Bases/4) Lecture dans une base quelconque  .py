def lire_base(base: int, chiffres: list) -> int:
    """Renvoie la valeur du nombre, avec ses 'chiffres' donnés en 'base'.
    >>> lire_base(12, [3, 11])
    47
    
    """
    résultat = 0
    for chiffre in chiffres:
        résultat *= base
        résultat += chiffre
    return résultat
base, nb_chiffres = map(int, input().split())
chiffres = map(int, input().split())
print(lire_base(base, chiffres))
