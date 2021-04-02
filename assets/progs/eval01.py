while True:
    mid = int(input("Montant initial distributeur (mid ≥ 0) ? "))
    if mid >= 0:
        break

while True:
    mma = int(input("Montant maximal autorisé (mma ≥ 10) ? "))
    if mma >= 10 and mma % 10 == 0:
        break

while True:
    n = int(input("Nombre de clients (1 ≤ n ≤ 15) ? "))
    if 1 <= n <= 15:
        break

retraits =  [0] * n
for i in range(n):
    while True:
        retraits[i] = int(input(f"Montant retrait client {i+1} ? "))
        if retraits[i] > 0:
            break

mr = mid
print("Les transactions invalides sont numéro : ")
for i in range(n):
    if retraits[i] % 10 != 0 or retraits[i] > mma or retraits[i] > mr:
        print(f"- {i+1} => {retraits[i]} DT")
    else:
        mr -= retraits[i]

print(f"Le montant restant = {mr} DT")