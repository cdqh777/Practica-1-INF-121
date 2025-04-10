package ejercicio3;

import java.util.ArrayList;
import java.util.List;

class Administrativo {
    private String nombre;
    private double sueldoMes;
    private String cargo;

    public Administrativo(String nombre, double sueldoMes, String cargo) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.cargo = cargo;
    }

    public double sueldoTotal() {
        return sueldoMes;
    }

    public boolean tieneSueldoMes(double x) {
        return sueldoMes == x;
    }

    @Override
    public String toString() {
        return String.format("Administrativo: %s, Sueldo Base: %.2f, Cargo: %s, Sueldo Total: %.2f",
                nombre, sueldoMes, cargo, sueldoTotal());
    }
}