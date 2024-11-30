"""Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100."""

numero = 0
suma = 0

while numero <= 100:
    suma += numero
    numero = numero + 1

print(f"La suma és: {suma}")