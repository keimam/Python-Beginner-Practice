from random import choice

nomer_togel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nomer_menang = []

for i in range(4):
    tarik_nomer = choice(nomer_togel)
    nomer_menang.append(tarik_nomer)

print(nomer_menang)
