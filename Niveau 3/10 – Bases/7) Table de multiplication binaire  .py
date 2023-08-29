def binaire(n: int) -> str:
    "Renvoie n écrit en binaire."
    return bin(n)[2:]
n = int(input())
for i in range(1, n+1):
    print("\t".join(binaire(i*j) for j in range(1, n+1)))