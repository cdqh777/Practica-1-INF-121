class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def calcularPromedio(self):
        return (self.nota_1 + self.nota_2) / 2

    def aprobo(self):
        return self.calcularPromedio() >= 6

    def __str__(self):
        return f"Estudiante: {self.nombre}, Notas: {self.nota_1} y {self.nota_2}"


estudiante1 = Estudiante("Juan Pérez", 7, 8)
estudiante2 = Estudiante("María García", 5, 6)
estudiante3 = Estudiante("Carlos López", 4, 3)

estudiantes = [estudiante1, estudiante2, estudiante3]

for estudiante in estudiantes:
    print(estudiante)
    print(f"Promedio: {estudiante.calcularPromedio() :.1f}")
    print(f"Aprobó: {'Sí' if estudiante.aprobo() else 'No'}\n")