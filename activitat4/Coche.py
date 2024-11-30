class Coche: 
    def __init__(self, nombre, modelo, marca, matricula, color):
        self.nombre = nombre
        self.modelo = modelo
        self.marca = marca
        self.matricula = matricula
        self.color = color

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, new_nombre):
        self.nombre = new_nombre

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, new_modelo):
        self.modelo = new_modelo

    def getMarca(self):
        return self.marca
    
    def setMarca(self, new_marca):
        self.marca = new_marca

    def getMatricula(self):
        return self.matricula
    
    def setMatricula(self, new_matricula):
        self.matricula = new_matricula

    def getColor(self):
        return self.color
    
    def setColor(self, new_color):
        self.color = new_color
