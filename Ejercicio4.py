"""Aplicar IVA segons el salari
En aquest exercici, s’aplicarà un IVA (0, 10, 21) segons el salari que s’indiqui.
Crear una variable de nom salari. Si el salari és menor de 15.000, s’aplica un 0% d’IVA. Si el salari és menor de 30.000 s’aplica un 10% de l’iva. Si el salari és menor a 60.000 s’aplica un IVA del 21%.

Exemple càlcul si el salari son 5000 => 5.000 * 0/100
"""

salario = 50000

if salario >= 0 and salario < 15000:
    print("No te cap IVA")

elif salario >= 15000 and salario < 30000:
    iva = salario * 0.10
    print(f"Té  {iva}  de IVA")

elif salario >= 30000 and salario < 60000:
    iva = salario * 0.21
    print(f"Té  {iva}  de IVA")

else:
    print("Valor incorrecto")
