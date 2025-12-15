from estructuras.ListaPrioridades import ListaCola 
from modelos.Solicitud import Solicitud

class ControladorSolicitudes:
    def __init__(self):

        self.cola_solicitudes = ListaCola()

    def agregar_solicitud(self, id, cliente, tipo, prioridad, cpu, ram, alm, tiempo):
        nueva_sol = Solicitud(id, cliente, tipo, prioridad, cpu, ram, alm, tiempo)
        self.cola_solicitudes.insertar_dato(nueva_sol, prioridad)
        print(f"Solicitud {id} agregada con prioridad {prioridad}.")

    def ver_cola(self):
        print("\n--- COLA DE SOLICITUDES (Por Prioridad) ---")
        if self.cola_solicitudes.esta_vacia(): 
            print("La cola está vacía.")
            return

        actual = self.cola_solicitudes.primero
        pos = 1
        while actual:
            sol = actual.dato
            print(f"{pos}. [{sol.prioridad}] {sol.cliente} - {sol.tipo} (ID: {sol.id})")
            actual = actual.siguiente
            pos += 1

    def procesar_siguiente(self):
        """Atiende la solicitud con mayor prioridad (la primera de la lista)"""
        if self.cola_solicitudes.primero is None:
            print("No hay solicitudes pendientes.")
            return

        solicitud_top = self.cola_solicitudes.primero.dato
        print(f"\nProcesando solicitud prioritaria: {solicitud_top.id} de {solicitud_top.cliente}")
        
        # Eliminar de la cola 
        self.cola_solicitudes.primero = self.cola_solicitudes.primero.siguiente
        self.cola_solicitudes.longitud -= 1
        
        print("Solicitud procesada y removida de la cola.")