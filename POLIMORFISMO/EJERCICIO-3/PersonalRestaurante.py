class Cocinero:
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora

    def sueldoTotal(self):
        return self.sueldoMes + (self.horasExtra * self.sueldoHora)

    def __str__(self):
        return f"Cocinero: {self.nombre}, Sueldo Base: {self.sueldoMes}, Horas Extra: {self.horasExtra}, Sueldo por Hora: {self.sueldoHora}, Sueldo Total: {self.sueldoTotal()}"

    def tieneSueldoMes(self, x):
        return self.sueldoMes == x


class Mesero:
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora, propina):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora
        self.propina = propina

    def sueldoTotal(self):
        return self.sueldoMes + (self.horasExtra * self.sueldoHora) + self.propina

    def __str__(self):
        return f"Mesero: {self.nombre}, Sueldo Base: {self.sueldoMes}, Horas Extra: {self.horasExtra}, Sueldo por Hora: {self.sueldoHora}, Propina: {self.propina}, Sueldo Total: {self.sueldoTotal()}"

    def tieneSueldoMes(self, x):
        return self.sueldoMes == x


class Administrative:
    def __init__(self, nombre, sueldoMes, cargo):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.cargo = cargo

    def sueldoTotal(self):
        return self.sueldoMes

    def __str__(self):
        return f"Administrativo: {self.nombre}, Sueldo Base: {self.sueldoMes}, Cargo: {self.cargo}, Sueldo Total: {self.sueldoTotal()}"

    def tieneSueldoMes(self, x):
        return self.sueldoMes == x


cocinero1 = Cocinero("Juan Pérez", 1200, 10, 15.5)
mesero1 = Mesero("Carlos Gómez", 900, 8, 10.0, 200)
mesero2 = Mesero("Ana López", 950, 5, 10.5, 180)
admin1 = Administrative("María Rodríguez", 1500.0, "Gerente")
admin2 = Administrative("Pedro Sánchez", 1300.0, "Contador")

print("\nSueldos totales de los empleados:")
print(cocinero1)
print(mesero1)
print(mesero2)
print(admin1)
print(admin2)


def SueldoX(empleados, x):
    return [emp for emp in empleados if emp.tieneSueldoMes(x)]


empleados = [cocinero1, mesero1, mesero2, admin1, admin2]
x = 900

print(f"\nEmpleados con sueldo base igual a {x}:")
for emp in SueldoX(empleados, x):
    print(emp)