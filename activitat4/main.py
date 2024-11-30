#Importamos los getters y setters
from Coche import Coche
from Colibri import Colibri

# Creación de la instancia
coche_1 = Coche("Renault", "Cenic", "146789", "4567JKL", "rojo")

#Imprimos los getters con un texto
print(f'Mi coche es un: {coche_1.getNombre()}')
print(f'El modelo de mi coche és: {coche_1.getModelo()}')
print(f'La matricula de mi coche és: {coche_1.getMatricula()}')
print("")

# Modificamos los setters para después imprimir los getters que se han modificado
print('Modificamos el nombre del coche y el modelo')
coche_1.setNombre('Seat')
coche_1.setModelo('Ibiza')
print(coche_1.getNombre())
print(coche_1.getModelo())
print("")



# Creación de la instancia

colibri_1 = Colibri("Picaflor", "200g", "colibri morado", "America", "blanco")

#Imprimos los getters con un texto
print(f'El nombre de mi colibri es: {colibri_1.getNombre()}')
print(f'El tamaño de mi colibri és de: {colibri_1.getTamaño()}')
print(f'El tipo de colibri que tengo es: {colibri_1.getTipos()}')
print(f'La procedencia de mi colibri es: {colibri_1.getProcedencia()}')
print("")

# Modificamos los setters para después imprimir los getters que se han modificado
print('Modificamos el tamaño y el tipo')
colibri_1.setTamaño('500g')
colibri_1.setTipos('Colibrí crestado')
print(colibri_1.getTamaño())
print(colibri_1.getTipos())









    
        