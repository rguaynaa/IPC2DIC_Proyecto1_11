from modelos.Contenedor import Contenedor

class controladorContenedores:
    def __init__(self,controlador_vm):
        self.controlador_vms = controlador_vm
    
    def desplegar_contenedores(self,id_vm,id_contenedor,nombre,cpu,ram,puerto):

        vm = self.controlador_vms.buscar_vm_id(id_vm)

        if vm:
            #validar recursos de la vm
            nuevo_contenedor = Contenedor(id_contenedor,nombre,cpu,ram,puerto)
            vm.contenedores.agregar_dato(nuevo_contenedor)
            print(f"Contenedor {nombre} desplegado en VM {id_vm}.")

    def listar_contenedores_vm(self,id_vm):
        vm = self.ctrl_vms.buscar_vm_por_id(id_vm)
        if vm:
            print("="*40)
            print(f"Contenedores en VM {id_vm}:")
            print("="*40)
            vm.contenedores.mostrar_informacion()