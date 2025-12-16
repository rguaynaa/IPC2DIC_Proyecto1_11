from modelos.Contenedor import Contenedor

class controladorContenedores:
    def __init__(self,controlador_vm):
        self.controlador_vms = controlador_vm
    
    def desplegar_contenedores(self,id_vm,id_contenedor,nombre,cpu,ram,puerto):

        vm = self.controlador_vms.buscar_vm_id(id_vm)

        if vm:
            disponible_cpu = vm.cpu_nucleos - vm.cpu_usados()
            disponible_ram = vm.ram_GB - vm.ram_usada()

            if disponible_cpu >= int(cpu) and disponible_ram >= int(ram):
                nuevo_contenedor = Contenedor(id_contenedor,nombre,int(cpu),int(ram),puerto)
                vm.contenedores.agregar_dato(nuevo_contenedor)
                print(f"Contenedor {nombre} desplegado en VM {id_vm}.")
            else:
                print(f"Error: Recursos insuficientes en VM {id_vm} para desplegar el contenedor {nombre}.")

    def listar_contenedores_vm(self,id_vm):
        vm = self.ctrl_vms.buscar_vm_por_id(id_vm)
        if vm:
            print("="*40)
            print(f"Contenedores en VM {id_vm}:")
            print("="*40)
            vm.contenedores.mostrar_informacion()
    
    def eliminar_contenedor(self,id_vm,id_contenedor):
        vm = self.controlador_vms.buscar_vm_id(id_vm)
        if vm:
            if vm.contenedores.eliminar_dato_por_id(id_contenedor,'id'):
                print(f"Contenedor {id_contenedor} eliminado de VM {id_vm}.")
            else:
                print(f"Error: Contenedor {id_contenedor} no encontrado en VM {id_vm}.")