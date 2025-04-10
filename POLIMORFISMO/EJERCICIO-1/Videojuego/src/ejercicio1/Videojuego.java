package ejercicio1;

public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    public Videojuego(String nombre, String plataforma) {
        this(nombre, plataforma, 1);
    }

    public static Videojuego nombrePlataforma(String nombre, String plataforma) {
        return new Videojuego(nombre, plataforma);
    }

    public void mostrar() {
        System.out.println("Videojuego: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Jugadores: " + cantidadJugadores);
        System.out.println("--------------------");
    }

    public void agregarJugadores(int cantidad) {
        if (cantidad > 0) {
            cantidadJugadores += cantidad;
        } else {
            System.out.println("La cantidad debe ser mayor a cero");
        }
    }

    public void agregarJugadores() {
        agregarJugadores(1);
    }

    public static void main(String[] args) {
        Videojuego juego1 = new Videojuego("The Legend of Zelda", "Nintendo Switch", 1);
        Videojuego juego2 = Videojuego.nombrePlataforma("Minecraft", "PC");

        System.out.println("Videojuegos creados:");
        juego1.mostrar();
        juego2.mostrar();

        System.out.println("\nAgregando jugadores:");
        juego2.agregarJugadores(3);

        System.out.println("\nDespués de agregar jugadores:");
        juego1.mostrar();
        juego2.mostrar();
    }
}