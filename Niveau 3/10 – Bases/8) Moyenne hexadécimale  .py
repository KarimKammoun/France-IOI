def int16(chaîne: str) -> int:
    n = 0
    for c in chaîne:
        n *= 16
        if "0" <= c <= "9":
            n += ord(c) - ord('0')
        else:
            n += ord(c) - ord('A') + 10
    return n
def hexadécimal(n: int) -> str:
    if n == 0:
        return "0"
    chiffres = []
    while n > 0:
        chiffre = n % 16
        n = n // 16
        chiffres.append(chiffre)
    table = "0123456789ABCDEF"
    return "".join(table[chiffre] for chiffre in chiffres[::-1])
n = int16(input())
somme = sum(int16(input()) for _ in range(n))
print(hexadécimal(somme // n))