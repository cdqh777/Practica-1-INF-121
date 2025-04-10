class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")

    def es_mayor_de_edad(self):
        return self.edad >= 18


persona1 = Persona("Juan", 25, "Tarija")
persona2 = Persona("Ana", 17, "Cochabamba")
persona3 = Persona("Carlos", 30, "La Paz")

persona1.saludar()
persona2.saludar()
persona3.saludar()

print(f"\n¿{persona1.nombre} es mayor de edad? {persona1.es_mayor_de_edad()}")
print(f"¿{persona2.nombre} es mayor de edad? {persona2.es_mayor_de_edad()}")
print(f"¿{persona3.nombre} es mayor de edad? {persona3.es_mayor_de_edad()}")