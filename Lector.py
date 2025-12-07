import xml.etree.ElementTree as ET
from modelos.CentroDatos import CentroDatos

class Lector:
    def __init__(self):
        self.centros = []
    
    def cargar_archivo_xml(self, ruta_archivo):
        try:
            tree = ET.parse(ruta_archivo)
            ruta = tree.getroot()

            self.cargar_centros(ruta)
            self.cargar_vms(ruta)
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

            centro = CentroDatos(id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento)

            self.centros.append(centro)
            print(f"Centro {id_centro} cargado exitosamente.")

        for c in self.centros:
            c.mostrar_datos()


    def cargar_maquinas_virtuales(self,root):
        maquinas_xml = root.find('.//maquinasVirtuales')



        
            
                
                

        
        






            

            
