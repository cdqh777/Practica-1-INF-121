package ejercicio3;

import java.util.ArrayList;
import java.util.List;

class Mesero {
    private String nombre;
    private double sueldoMes;
    private int horasExtra;
    private double sueldoHora;
    private double propina;

    public Mesero(String nombre, double sueldoMes, int horasExtra, double sueldoHora, double propina) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }

    public double sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora) + propina;
    }

    public boolean tieneSueldoMes(double x) {
        return sueldoMes == x;
    }

    @Override
    public String toString() {
        return String.format("Mesero: %s, Sueldo Base: %.2f, Horas Extra: %d, Sueldo por Hora: %.2f, Propina: %.2f, Sueldo Total: %.2f",
                nombre, sueldoMes, horasExtra, sueldoHora, propina, sueldoTotal());
    }
}
