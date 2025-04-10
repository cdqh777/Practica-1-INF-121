class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        return "¡Guau!"

    def moverse(self):
        return f"{self.nombre} está corriendo"


class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        return "¡Miau!"

    def moverse(self):
        return f"{self.nombre} está saltando"


class Pajaro:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        return "¡Pío pío!"

    def moverse(self):
        return f"{self.nombre} está volando"


mi_perro = Perro("Max")
mi_gato = Gato("Lolo")
mi_pajaro = Pajaro("Piolín")

print(mi_perro.hacerSonido())
print(mi_gato.hacerSonido())
print(mi_pajaro.hacerSonido())

print(mi_perro.moverse())
print(mi_gato.moverse())
print(mi_pajaro.moverse())