package ejercicio3;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static List<Object> sueldoX(List<Object> empleados, double x) {
        List<Object> resultado = new ArrayList<>();
        for (Object emp : empleados) {
            if (emp instanceof Cocinero && ((Cocinero) emp).tieneSueldoMes(x)) {
                resultado.add(emp);
            } else if (emp instanceof Mesero && ((Mesero) emp).tieneSueldoMes(x)) {
                resultado.add(emp);
            } else if (emp instanceof Administrativo && ((Administrativo) emp).tieneSueldoMes(x)) {
                resultado.add(emp);
            }
        }
        return resultado;
    }

    public static void main(String[] args) {
        Cocinero cocinero1 = new Cocinero("Juan Pérez", 1200, 10, 15.5);
        Mesero mesero1 = new Mesero("Carlos Gómez", 900, 8, 10.0, 200);
        Mesero mesero2 = new Mesero("Ana López", 950, 5, 10.5, 180);
        Administrativo admin1 = new Administrativo("María Rodríguez", 1500.0, "Gerente");
        Administrativo admin2 = new Administrativo("Pedro Sánchez", 1300.0, "Contador");

        System.out.println("\nSueldos totales de los empleados:");
        System.out.println(cocinero1);
        System.out.println(mesero1);
        System.out.println(mesero2);
        System.out.println(admin1);
        System.out.println(admin2);

        List<Object> empleados = new ArrayList<>();
        empleados.add(cocinero1);
        empleados.add(mesero1);
        empleados.add(mesero2);
        empleados.add(admin1);
        empleados.add(admin2);

        double x = 900;
        System.out.printf("\nEmpleados con sueldo base igual a %.2f:\n", x);
        for (Object emp : sueldoX(empleados, x)) {
            System.out.println(emp);
        }
    }
}