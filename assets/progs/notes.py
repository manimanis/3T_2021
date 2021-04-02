# Un enseignant au lycée veut écrire un programme qui :
# (1) Saisit le nombre des élèves n, (3 ≤ n ≤ 36)
while True:
    n = int(input("Donner le nombre (3 ≤ n ≤ 36) ? "))
    if 3 <= n <= 36:
        break

# (2) Saisit les notes des élèves dans un tableau notes.
# Vérifier que les notes sont dans l'intervalle [0, 20].
notes = [0.0] * n
for i in range(n):
    while True:
        r = 'er' if i+1 == 1 else 'ème'
        notes[i] = float(input(f'Note du {i+1}{r} élève ? '))
        if 0.0 <= notes[i] <= 20.0:
            break

# (3) Déterminer la moyenne de la classe moy.
s = 0
for i in range(n):
    s = s + notes[i]
moy = s / n
print("La moyenne de la classe est :", moy)

# (4) Calculer la meilleure notemax et la pire note notemin.
notemax = notes[0]
for i in range(1, n):
    if notes[i] > notemax:
        notemax = notes[i]
print("La meilleure note est :", notemax)

notemin = notes[0]
for i in range(1, n):
    if notes[i] < notemin:
        notemin = notes[i]
print("La pire note est :", notemin)

# (5) Calculer le nombre d'élèves :
# - nbr_moy qui ont obtenu au dessus de la moyenne.
# - nbr_el qui ont obtenu une note au dessus de la moyenne de la classe moy.
nbr_moy = 0
for i in range(n):
    if notes[i] >= 10:
        nbr_moy = nbr_moy + 1
print("Le nombre d'élèves qui ont obtenu au dessus de 10 :", nbr_moy)

nbr_el = 0
for i in range(n):
    if notes[i] >= moy:
        nbr_el = nbr_el + 1
print("Le nombre d'élèves qui ont obtenu au dessus de", moy, ":", nbr_el)

# (6) Calculer le nombre de notes par intervalles.
# [0, 5[
# [5, 10[
# [10, 15[
# [15, 20[
# [20, +∞[
nb_nt = [0] * 5
for i in range(n):
    intervalle = int(notes[i]) // 5
    nb_nt[intervalle] = nb_nt[intervalle] + 1

for i in range(5):
    print(f"Nombre de notes entre [{i*5}, {(i+1)*5}[ : {nb_nt[i]}")