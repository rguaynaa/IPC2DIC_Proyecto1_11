class Solicitud:
    def __init__(self, id, cliente, tipo, prioridad, cpu, ram_GB, almacenamiento_GB, tiempo_estimado):
        self.id = id
        self.cliente = cliente
        self.tipo = tipo
        self.prioridad = prioridad
        self.cpu = cpu
        self.ram_GB = ram_GB
        self.almacenamiento_GB = almacenamiento_GB
        self.tiempo_estimado = tiempo_estimado
        self.estado = "Pendiente"
    
    def mostrar_datos(self):
        print(f'\nSolicitud: {self.id} - {self.cliente} ({self.tipo}) - Prioridad: {self.prioridad} \nEstado: {self.estado} \nRecursos: CPU={self.cpu}, RAM={self.ram_GB}')