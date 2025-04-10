package ejercicio3;

import java.util.ArrayList;
import java.util.List;

class Cocinero {
    private String nombre;
    private double sueldoMes;
    private int horasExtra;
    private double sueldoHora;

    public Cocinero(String nombre, double sueldoMes, int horasExtra, double sueldoHora) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }

    public double sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora);
    }

    public boolean tieneSueldoMes(double x) {
        return sueldoMes == x;
    }

    public String toString() {
        return String.format("Cocinero: %s, Sueldo Base: %.2f, Horas Extra: %d, Sueldo por Hora: %.2f, Sueldo Total: %.2f",
                nombre, sueldoMes, horasExtra, sueldoHora, sueldoTotal());
    }
}
