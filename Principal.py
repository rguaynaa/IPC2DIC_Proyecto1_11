from Lector import Lector

def menu_principal():
    lector = Lector()
    ruta = ''
    while True:
        print('\n--------- MENU PRINCIPAL ---------')
        print('- 1. Carga Archivo XML -')
        print('- 2. Gestion de Centros de Datos -')
        print('- 3. Gestión de Máquinas Virtuales  -')
        print('- 4. Gestión de Contenedores) -')
        print('- 5. Gestión de Solicitudes -')
        print('- 6. Salir -')
        print('----------------------------------')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 1:
                ruta = cargar_xml('entrada')
                if ruta == '':
                    print('Error: No se seleccionó un archivo')
                else:
                    print('Archivo de centros cargado exitosamente')
                    print(ruta)
            case 2:
                lector.cargar_archivo_xml(ruta)
            case 3:
                pass
                #leer_reservaciones_parse(ruta_reservaciones)
            case 4:
                pass
                #escribirConMiniDOM()
            case 5:
                pass
                #escribirConET()
            case 6:
                print('Hasta luego')
                break
            case _:
                print('Opción no válida')


def cargar_xml(tipo):
    nombre_archivo = input(f'Ingrese el nombre del archvo "{tipo}.xml": ').strip()
    if nombre_archivo == '':
        return ''
    ruta_archivo = f'{nombre_archivo}'
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            pass
        return ruta_archivo
    except FileNotFoundError:
        print(f'Archivo no encontrado: {ruta_archivo}')
        return ''
    

if __name__ == '__main__':
    menu_principal()