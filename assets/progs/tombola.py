from random import randint

# Saisie du nombre de participants
while True:
    n = int(input("Donner le nombre de participants (5 ≤ n ≤ 20) ? "))
    if 5 <= n <= 20:
        break

# Déclaration du tableau de participants
noms = [""] * n

# Saisie des noms
for i in range(n):
    noms[i] = input(f"Donner le nom du {i+1}ème participant ? ")

# Nombre maximal de prix
nmp = int(n > 10) * 10 + int(n <= 10) * n

# Saisie du nombre de prix
while True:
    np = int(input(f"Donner le nombre de prix (1 ≤ np ≤ {nmp}) ? "))
    if 1 <= np <= nmp:
        break

# Déclaration du tableau des prix
prix = [""] * np

# Saisie des noms
for i in range(np):
    prix[i] = input(f"Donner le nom du {i+1}ème prix ? ")

# Tirage au sort
for i in range(n):
    j = randint(0, n-1)
    noms[i], noms[j] = noms[j], noms[i]

# Affichage des gagnants
for i in range(np):
    print(noms[i], "gagne", prix[i])