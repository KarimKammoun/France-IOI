def main():
    binaire = input()
    n = 0
    for bit in binaire:
        n <<= 1
        if bit == '1':
            n += 1
    print(n)
main() 
