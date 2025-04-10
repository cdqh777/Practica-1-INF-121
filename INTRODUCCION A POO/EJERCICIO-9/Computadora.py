class Computadora:
    def __init__(self):
        self.estado = "Apagado"
        self.componentes = {
            "CPU": "Intel i7",
            "RAM": "16GB DDR4",
            "Almacenamiento": "SSD 512GB",
            "GPU": "NVIDIA RTX 3060",
            "Sistema Operativo": "Windows 10"
        }

    def encender(self):
        if self.estado == "Apagado":
            self.estado = "Encendido"
            return "La computadora se ha encendido"
        return "La computadora ya está encendida"

    def apagar(self):
        if self.estado == "Encendido":
            self.estado = "Apagado"
            return "La computadora se ha apagado"
        return "La computadora ya está apagada"

    def mostrar_estado(self):
        return f"Estado actual: {self.estado}"

    def mostrar_componentes(self):
        print("Componentes principales:")
        for nombre, espec in self.componentes.items():
            print(f"- {nombre}: {espec}")


mi_pc = Computadora()
print(mi_pc.mostrar_estado())
mi_pc.mostrar_componentes()

print(mi_pc.encender())
print(mi_pc.mostrar_estado())

print(mi_pc.apagar())
print(mi_pc.mostrar_estado())
