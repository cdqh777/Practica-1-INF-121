package ejercicio1;

public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public void saludar() {
        System.out.println("Hola, soy " + this.nombre + " de " + this.ciudad);
    }

    public boolean esMayorDeEdad() {
        return this.edad >= 18;
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 25, "Tarija");
        Persona persona2 = new Persona("Ana", 17, "Cochabamba");
        Persona persona3 = new Persona("Carlos", 30, "La Paz");

        persona1.saludar();
        persona2.saludar();
        persona3.saludar();

        System.out.println("\n¿" + persona1.nombre + " es mayor de edad? " + persona1.esMayorDeEdad());
        System.out.println("¿" + persona2.nombre + " es mayor de edad? " + persona2.esMayorDeEdad());
        System.out.println("¿" + persona3.nombre + " es mayor de edad? " + persona3.esMayorDeEdad());
    }
}