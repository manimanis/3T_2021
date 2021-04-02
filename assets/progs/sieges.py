from random import randint

# (1) Saisit le nombre total de sièges disponibles (10 ≤ nts ≤ 30)
while True:
    nts = int(input("Donner le nombre de sièges (10 ≤ nts ≤ 30) ? "))
    if 10 <= nts <= 30:
        break

# (2) Saisit le nombre de sièges réservés (1 ≤ nsr ≤ nts)
while True:
    nsr = int(input(f"Donner le nombre de sièges réservés (1 ≤ nsr ≤ {nts}) ? "))
    if 1 <= nsr <= nts:
        break

#(3) Remplit un tableau res par les numéros des sièges réservés
# d'une façon aléatoire et sans répétitions
res = [0] * nsr
for i in range(nsr):
    while True:
        ns = randint(1, nsr)
        if not ns in res:
            break
    res[i] = ns

# (4) Détermine les numéros des sièges libres dans un tableau lib, 
# ainsi que le nombre de sièges libre nsl
nsl = nts - len(res)
lib = [0] * nsl
j = 0
for i in range(nts):
    if not (i+1) in res:
        lib[j] = i+1
        j += 1

# (5) Afficher les numéros des sièges réservés
print("Les sièges réservés : ")
for i in range(nsr):
    print(res[i], end=', ')
print()

# Afficher les numéros des sièges libres
print("Les sièges libre : ")
for i in range(nsl):
    print(lib[i], end=', ')
print()
