def main():
    n = int(input())
    puissance = 1
    while puissance <= n:
        puissance <<= 1
    puissance >>= 1
    print(puissance)
main()