class Oficina:
    def __init__(self, nroSillas, nroEscritorios, nroEstanterias):
        self.nroSillas = nroSillas
        self.nroEscritorios = nroEscritorios
        self.nroEstanterias = nroEstanterias

    def mostrar(self):
        print("Oficina:")
        print(f"- Sillas: {self.nroSillas}")
        print(f"- Escritorios: {self.nroEscritorios}")
        print(f"- Estanterías: {self.nroEstanterias}")

    def cantidadMuebles(self):
        return self.nroSillas + self.nroEscritorios + self.nroEstanterias


class Aula:
    def __init__(self, nombre, capacidad, nropupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nropupitres = nropupitres

    def mostrar(self):
        print(f"Aula {self.nombre}:")
        print(f"- Capacidad: {self.capacidad}")
        print(f"- Pupitres: {self.nropupitres}")

    def cantidadMuebles(self):
        return self.nropupitres


class Laboratorio:
    def __init__(self, nombre, capacidad, nroMesas, nroSillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nroMesas = nroMesas
        self.nroSillas = nroSillas

    def mostrar(self):
        print(f"Laboratorio {self.nombre}:")
        print(f"- Capacidad: {self.capacidad}")
        print(f"- Mesas: {self.nroMesas}")
        print(f"- Sillas: {self.nroSillas}")

    def cantidadMuebles(self):
        return self.nroMesas + self.nroSillas


oficina1 = Oficina(10, 5, 3)
oficina2 = Oficina(8, 4, 2)

aula1 = Aula("A101", 30, 25)
aula2 = Aula("B205", 40, 35)

laboratorio1 = Laboratorio("L302", 20, 10, 20)

print("\nMostrando información de los ambientes:")
oficina1.mostrar()
print()
oficina2.mostrar()
print()
aula1.mostrar()
print()
aula2.mostrar()
print()
laboratorio1.mostrar()

print("\nCantidad de muebles por ambiente:")
print(f"Oficina 1: {oficina1.cantidadMuebles()} muebles")
print(f"Oficina 2: {oficina2.cantidadMuebles()} muebles")
print(f"Aula {aula1.nombre}: {aula1.cantidadMuebles()} muebles")
print(f"Aula {aula2.nombre}: {aula2.cantidadMuebles()} muebles")
print(f"Laboratorio {laboratorio1.nombre}: {laboratorio1.cantidadMuebles()} muebles")