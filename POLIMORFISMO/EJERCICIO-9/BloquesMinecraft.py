class BloqueCofre:
    def __init__(self, capacidad, resistencia):
        self.tipo = "cofre"
        self.capacidad = capacidad
        self.resistencia = resistencia

    def accion(self):
        print(f"Abriendo cofre con capacidad de {self.capacidad} items")

    def colocar(self, orientacion="suelo"):
        print(f"Cofre colocado en {orientacion}")

    def romper(self):
        print(f"Rompiendo cofre con resistencia {self.resistencia}:")
        print("Los items pueden caer al suelo")


class BloqueTnt:
    def __init__(self, daño):
        self.tipo = "TNT"
        self.daño = daño

    def accion(self):
        print(f"Activando TNT que causará {self.daño} puntos de daño")

    def colocar(self, orientacion="suelo"):
        print(f"TNT colocada en {orientacion}")

    def romper(self):
        print("Rompiendo bloque de TNT:")
        print("La TNT ha explotado causando daño")


class BloqueHorno:
    def __init__(self, color, capacidad_comida):
        self.tipo = "horno"
        self.color = color
        self.capacidad_comida = capacidad_comida

    def accion(self):
        print(f"Usando horno {self.color} para cocinar {self.capacidad_comida} alimentos")

    def colocar(self, orientacion="suelo"):
        print(f"Horno {self.color} colocado en {orientacion}")

    def romper(self):
        print(f"Rompiendo horno {self.color}:")
        print("Suelta carbón y los items cocinados")


cofre1 = BloqueCofre(27, 10)
cofre2 = BloqueCofre(54, 15)

tnt1 = BloqueTnt(10)
tnt2 = BloqueTnt(20)

horno1 = BloqueHorno("negro", 3)
horno2 = BloqueHorno("gris", 5)

print("\nProbando método accion:")
cofre1.accion()
tnt1.accion()
horno1.accion()

print("\nProbando método colocar:")
cofre2.colocar()
tnt2.colocar("pared")
horno2.colocar("techo")

print("\nProbando método romper:")
cofre1.romper()
tnt2.romper()
horno2.romper()