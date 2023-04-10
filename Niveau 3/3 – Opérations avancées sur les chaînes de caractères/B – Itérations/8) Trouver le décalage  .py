def déchiffre(lettre: str, clé: int) -> str:
    def tourne_autour(lettre, pivot, clé):
        indice = ord(lettre) - ord(pivot)
        indice_déchiffré = (indice - clé) % 26
        return chr(ord(pivot) + indice_déchiffré)
    
    if 'a' <= lettre <= 'z':
        return tourne_autour(lettre, 'a', clé) 
    elif 'A' <= lettre <= 'Z':
        return tourne_autour(lettre, 'A', clé) 
    else:
        return lettre    
CONST_fr_indice_freq_max = ord('E') - ord('A')
CONST_taille_alphabet = 26
texte = input()
fréquence_lettre = [0 for _ in range(CONST_taille_alphabet)]
fréquence_max = 0
indice_max = -1
for lettre in texte.upper():
    if 'A' <= lettre <= 'Z':
        indice = ord(lettre) - ord('A')
        fréquence_lettre[indice] += 1
        if fréquence_lettre[indice] > fréquence_max:
            fréquence_max = fréquence_lettre[indice]
            indice_max = indice
clé = (indice_max - CONST_fr_indice_freq_max) % CONST_taille_alphabet
print("".join(déchiffre(lettre, clé) for lettre in texte))