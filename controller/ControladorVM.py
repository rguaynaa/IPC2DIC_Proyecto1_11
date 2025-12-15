from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class ControladorVM: 
    def __init__(self):
        self.lista_vm = ListaSimpleEnlazada()

    def crear_vm(self,vm):
        self.lista_vm.agregar_dato(vm)
    
    def mostrar_vm(self):
        self.lista_vm.mostrar_informacion()
    
    def buscar_vm_id(self,id_vm):
        vm=self.lista_vm.buscar_dato_por_id(id_vm,'id')
        return vm
    
    def mostrar_vm_por_id(self, id_vm):
        vm = self.buscar_vm_id(id_vm)
        if vm:
            print("VM encontrada:")
            vm.mostrar_datos()
        else:
            print(f"Error: La VM {id_vm} no existe en el sistema o esta mal redactada.")

    def listar_vms_de_centro(self, controlador_centros, id_centro):

        centro = controlador_centros.lista_centros.buscar_dato_por_id(id_centro, 'id')
        if centro:
            print(f"\n--- LISTADO DE VMS EN {centro.nombre} ---")

            centro.vm.mostrar_informacion()
        else:
            print(f"Error: El centro {id_centro} no existe.")

    def migrar_vm(self, controlador_centros, id_vm, id_centro_destino):
        
        vm = self.buscar_vm_id(id_vm)# buscammos la vm globalmente(entre todos los centros)
        if not vm:
            print(f"Error: VM {id_vm} no encontrada.")
            return

        centro_origen = controlador_centros.lista_centros.buscar_dato_por_id(vm.id_centro, 'id')#buscamos el centro de origen de la vm
        centro_destino = controlador_centros.lista_centros.buscar_dato_por_id(id_centro_destino, 'id')#buscamos el centro destino

        if not centro_origen or not centro_destino:
            print("Error: Centro de origen o destino no válidos o no existen.")
            return
        
        #validar recursos en el centro destino

        #falta eliminar la vm del centro origen
    


