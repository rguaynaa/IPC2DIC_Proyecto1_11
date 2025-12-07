import xml.etree.ElementTree as ET
from modelos.CentroDatos import CentroDatos
from modelos.MaquinaVirtual import MaquinaVirtual
from modelos.Contenedor import Contenedor
from modelos.Solicitud import Solicitud

class Lector:
    def __init__(self):
        self.list_centros = []
        self.list_mv = []
        self.list_cont = []
        self.list_solicitud = []
    
    def cargar_archivo_xml(self, ruta_archivo):
        try:
            tree = ET.parse(ruta_archivo)
            ruta = tree.getroot()

            self.cargar_centros(ruta)
            self.cargar_maquinas_virtuales(ruta)
            self.cargar_solicitudes(ruta)
            self.cargar_instrucciones(ruta)
            return True, "Archivos cargados exitosamente"
        
        except Exception as e:
            return False,f"Error al cargar el archivo {str(e)}"
    
    def cargar_centros(self, root):
        centros_xml = root.find('.//centrosDatos')
        if centros_xml is None:
            return
        
        for centro in centros_xml.findall('centro'):

            id_centro = centro.get('id')
            nombre = centro.get('nombre')

            ubicacion = centro.find('ubicacion')
            pais = ubicacion.find('pais').text
            ciudad = ubicacion.find('ciudad').text

            capacidad = centro.find('capacidad')
            cpu = int(capacidad.find('cpu').text)
            ram = int(capacidad.find('ram').text)
            almacenamiento = int(capacidad.find('almacenamiento').text)

            nuevo_centro = CentroDatos(id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento)

            self.list_centros.append(nuevo_centro)
            print(f"Centro {id_centro} cargado exitosamente.")

        for c in self.list_centros:
            c.mostrar_datos()


    def cargar_maquinas_virtuales(self,root):
        maquinas_xml = root.find('.//maquinasVirtuales')
        if maquinas_xml is None:
            return
        
        for maquina in maquinas_xml.findall('vm'):

            id_mv = maquina.get('id')
            id_centro = maquina.get('centroAsignado')
            so = maquina.find('sistemaOperativo').text

            recursos = maquina.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            almacenamiento = int(recursos.find('almacenamiento').text)

            ip = maquina.find('ip').text

            nueva_mv = MaquinaVirtual(id_mv,id_centro,so,cpu,ram,almacenamiento,ip)

            
            self.list_mv.append(nueva_mv)
            print(f"MaquinaVirtual {id_mv} cargado exitosamente.")

            if self.list_mv is None:
                print("Hubo un error al cargar el archivo.")
            else:
                contenedores =  maquina.find('contenedores')
                for cont in contenedores.findall('contenedor'):
                    id_cont = cont.get('id')
                    nombre = cont.find('nombre').text
                    imagen = cont.find('imagen').text

                    recursos = cont.find('recursos')
                    cpu = int(recursos.find('cpu').text)
                    ram = int(recursos.find('ram').text)
                    puerto = cont.find('puerto').text

                    nuevo_cont = Contenedor(id_cont,nombre,imagen,cpu,ram,puerto)

                    self.list_cont.append(nuevo_cont)

                    print(f"Contenedor {id_cont} cargado exitosamente.")
                
        for mv in self.list_mv:
            mv.mostrar_datos()

        print()

        for cont in self.list_cont:
            cont.mostrar_datos()


    def cargar_solicitudes(self,root):
        solicitudes_xml = root.find('.//solicitudes')
        if solicitudes_xml is None:
            return
        
        for sol in solicitudes_xml.findall('solicitud'):
            id_sol = sol.get('id')

            cliente = sol.find('cliente').text
            tipo = sol.find('cliente').text
            prioridad = int(sol.find('prioridad').text)

            recursos = sol.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            almacenamiento = int(recursos.find('almacenamiento').text)

            tiempo = int(sol.find('tiempoEstimado').text)

            nueva_solicitud = Solicitud(id_sol,cliente,tipo,prioridad,cpu,ram,almacenamiento,tiempo)

            self.list_solicitud.append(nueva_solicitud)
            print(f"Solicitud {id_sol} cargado exitosamente.")
        
        for sol in self.list_solicitud:
            sol.mostrar_datos()


    





        
            
                
                

        
        






            

            
