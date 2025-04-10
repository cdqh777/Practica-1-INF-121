class Celular:
    def __init__(self):
        self.espacio_total = 1024
        self.espacio_disponible = 1024
        self.max_aplicaciones = 20
        self.aplicaciones = []
        self.bateria = 100
        self.encendido = True

    def instalar_aplicacion(self, nombre, peso):
        if not self.encendido:
            return "El celular está apagado"
        if len(self.aplicaciones) >= self.max_aplicaciones:
            return "No hay espacio para más aplicaciones"
        if peso > self.espacio_disponible:
            return "No hay suficiente espacio de almacenamiento"

        self.aplicaciones.append({'nombre': nombre, 'peso': peso})
        self.espacio_disponible -= peso
        return f"Aplicación {nombre} instalada correctamente"

    def usar_aplicacion(self, nombre, minutos):
        if not self.encendido:
            return "El celular está apagado"

        for app in self.aplicaciones:
            if app['nombre'] == nombre:
                if app['peso'] > 250:
                    consumo = (minutos / 10) * 5
                elif app['peso'] > 100:
                    consumo = (minutos / 10) * 2
                else:
                    consumo = (minutos / 10) * 1

                if self.bateria <= consumo:
                    self.bateria = 0
                    self.encendido = False
                    return "Celular apagado"
                else:
                    self.bateria -= consumo
                    return f"Usando {nombre}. Batería restante: {self.bateria:.1f}%"

        return "Aplicación no encontrada"

    def estado_bateria(self):
        return f"Batería: {self.bateria:.1f}%"

    def listar_aplicaciones(self):
        return [app['nombre'] for app in self.aplicaciones]

    def cargar_bateria(self, porcentaje):
        if not self.encendido:
            self.encendido = True
        self.bateria = min(100, self.bateria + porcentaje)
        return f"Batería cargada al {self.bateria:.1f}%"


if __name__ == "__main__":
    mi_celular = Celular()

    print(mi_celular.instalar_aplicacion("WhatsApp", 120))
    print(mi_celular.instalar_aplicacion("Instagram", 270))

    print("\nAplicaciones instaladas:", mi_celular.listar_aplicaciones())
    print("Espacio disponible:", mi_celular.espacio_disponible, "MB")

    print("\n", mi_celular.usar_aplicacion("WhatsApp", 170))
    print("\n", mi_celular.usar_aplicacion("Instagram", 135))
    print(mi_celular.estado_bateria())

    print("Estado del celular:", "Encendido" if mi_celular.encendido else "Apagado")