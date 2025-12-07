
class CentroDatos:
    def __init__(self,id_centro,nombre,pais,ciudad,cpu_total,ram_total,almacenamiento_total):
        self.id = id_centro
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.cpu_total = cpu_total
        self.ram_total = ram_total
        self.almacenamiento_total = almacenamiento_total
        self.vm = [] # Acá es donde se va almacemar las Maquinas Virtuales cambiar a lista enlazada.

    
    def mostrar_datos(self):
        print(f'\nCentro: {self.nombre} ({self.id}) - {self.pais}, {self.ciudad} \nUbicacion: {self.pais}, {self.ciudad} \nCPU: {self.cpu_total} \nRAM: {self.ram_total} \nAlmacen {self.almacenamiento_total}')