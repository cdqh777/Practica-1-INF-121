class Videojuego:
    def __init__(self, nombre, plataforma, cantidadJugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores

    def nombrePlataforma(nombre, plataforma):
        return Videojuego(nombre, plataforma)


    def mostrar(self):
        print(f"Videojuego: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Jugadores: {self.cantidadJugadores}")
        print("-" * 20)

    def agregarJugadores(self, cantidad=1):
        if cantidad > 0:
            self.cantidadJugadores += cantidad
        else:
            print("La cantidad debe ser mayor a cero")


juego1 = Videojuego("The Legend of Zelda", "Nintendo Switch", 1)
juego2 = Videojuego.nombrePlataforma("Minecraft", "PC")

print("Videojuegos creados:")
juego1.mostrar()
juego2.mostrar()

print("\nAgregando jugadores:")
juego2.agregarJugadores(3)

print("\nDespués de agregar jugadores:")
juego1.mostrar()
juego2.mostrar()