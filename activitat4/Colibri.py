
class Colibri: 
    def __init__(self, nombre, tamaño, tipos, procedencia, color):
        self.nombre = nombre
        self.tamaño = tamaño
        self.tipos = tipos
        self.procedencia = procedencia
        self.color = color

    def getNombre(self):
        return self.nombre
    def setNombre(self, new_nombre):
        self.nombre = new_nombre

    def getTamaño(self):
        return self.tamaño
    def setTamaño(self, new_tamaño):
        self.tamaño = new_tamaño

    def getTipos(self):
        return self.tipos
    def setTipos(self, new_tipos):
        self.tipos = new_tipos

    def getProcedencia(self):
        return self.procedencia
    def setProcedencia(self, new_procedencia):
        self.procedencia = new_procedencia

    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color