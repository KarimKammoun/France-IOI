def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    binaire = []
    while n != 0:
        binaire.append(n&1)
        n >>= 1
    for x in binaire[::-1]:
        print(x, end="")
    print()
main()