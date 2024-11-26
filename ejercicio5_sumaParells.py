"""Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells."""

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
suma_pares = 0
suma_impares = 0

for i in num:
    if i % 2 == 0:
        suma_pares += i

    else:
        suma_impares += i

print(f"Suma pares = {suma_pares}")
print(f"Suma impares = {suma_impares}")