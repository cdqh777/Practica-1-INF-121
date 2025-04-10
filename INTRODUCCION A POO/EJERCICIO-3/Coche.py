class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad = max(0, self.velocidad - 5)

    def __str__(self):
        return f"{self.marca} {self.modelo} - Velocidad: {self.velocidad} km/h"


coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")

coche1.acelerar()
coche1.acelerar()

coche1.frenar()
coche2.frenar()

print(f"Coche 1: {coche1.marca} {coche1.modelo}, Velocidad: {coche1.velocidad} km/h")
print(f"Coche 2: {coche2.marca} {coche2.modelo}, Velocidad: {coche2.velocidad} km/h")