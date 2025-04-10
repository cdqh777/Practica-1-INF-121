package ejercicio2;

public class Coche {
    private String marca;
    private String modelo;
    private int velocidad;
    
    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = 0;
    }
    
    public void acelerar() {
        this.velocidad += 10;
    }
    
    public void frenar() {
        this.velocidad = Math.max(0, this.velocidad - 5);
    }
    
    @Override
    public String toString() {
        return marca + " " + modelo + " - Velocidad: " + velocidad + " km/h";
    }
    
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Ford", "Mustang");
        
        coche1.acelerar();
        coche2.acelerar();
        
        coche1.frenar();
        coche2.frenar();
        
        System.out.println("Coche 1: " + coche1.marca + " " + coche1.modelo + 
                          ", Velocidad: " + coche1.velocidad + " km/h");
        System.out.println("Coche 2: " + coche2.marca + " " + coche2.modelo + 
                          ", Velocidad: " + coche2.velocidad + " km/h");
    }
}