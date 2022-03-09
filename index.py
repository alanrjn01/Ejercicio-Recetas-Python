import shutil
from pathlib import Path
from os import system

def menu():
    print("---------------------")
    print("1:Leer receta\n2:Crear receta\n3:Crear categoría\n4:Eliminar receta\n5:Eliminar categoría\n6:Finalizar programa")
    opcion=0
    while opcion==0:
        opcion=int(input("Ingrese una opción: "))
        if opcion >=1 and opcion <=6:
            break
        opcion=0
    return opcion

def bienvenida_ruta_principal():
    print("¡Bienvenido!")
    # Obtengo la ruta donde se encuentra el programa
    ruta = Path().absolute()
    print(f"Nos encontramos en el directorio: {ruta}")
    contador_recetas = 0
    for indice, txt in enumerate(Path(ruta).glob("**/*.txt")):
        contador_recetas += 1
    print(f"Actualmente tienes {contador_recetas} recetas.")
    return ruta

def leer_receta(ruta_principal):
    # Creo una variable donde almaceno la ruta de Recetas:
    ruta_de_recetas = Path(ruta_principal,"Recetas")

    # Recorro la ruta de recetas mostrando el índice y nombre de subcarpetas:
    for indice,fichero in enumerate(ruta_de_recetas.iterdir()):
        print(indice,fichero.name)
    seleccion = int(input("Seleccione una carpeta: "))

    #A partir de la selección de usuario me posiciono en la ruta especificada
    for indice,fichero in enumerate(ruta_de_recetas.iterdir()):
        if seleccion == indice:
            ruta_receta_seleccionada = Path(ruta_de_recetas,Path(fichero))
            break;

    #Muestro los archivos dentro de la carpeta seleccionada
    for indice,fichero in enumerate(ruta_receta_seleccionada.iterdir()):
        #muestro el indice y el nombre del archivo sin la extensión
        print(indice,fichero.stem)
    seleccion_archivo = int(input("Seleccione una archivo: "))

    #Recorro los archivos buscando la coincidencia con la seleccion del usuario
    for indice,fichero in enumerate(ruta_receta_seleccionada.iterdir()):
        if seleccion_archivo == indice:
            ruta_archivo_seleccionado = Path(ruta_receta_seleccionada,Path(fichero))
            #leo el archivo seleccionado
            print(ruta_archivo_seleccionado.read_text())
            break;

def crear_receta(ruta_principal):
    # Creo una variable donde almaceno la ruta de Recetas:
    ruta_de_recetas = Path(ruta_principal, "Recetas")

    # Recorro la ruta de recetas mostrando el índice y nombre de subcarpetas:
    for indice, fichero in enumerate(ruta_de_recetas.iterdir()):
        print(indice, fichero.name)
    seleccion = int(input("Seleccione una carpeta: "))

    # A partir de la selección de usuario me posiciono en la ruta especificada
    for indice, fichero in enumerate(ruta_de_recetas.iterdir()):
        if seleccion == indice:
            ruta_crear_receta_seleccionada = Path(ruta_de_recetas, Path(fichero))
            break

    nombre_receta = input("Ingrese el nombre para su receta: ")

    # Creo una archivo txt en la ruta con el nombre ingresado por el usuario y luego lo instancio en una variable
    ruta_receta_creada = Path(ruta_crear_receta_seleccionada,Path(f"{nombre_receta}.txt"))

    #Ingreso de contenido en el archivo a partir de una variable con el texto ingresado por el usuario
    ingreso_receta = input("Ingrese el contenido de su receta:\n")
    ruta_receta_creada.write_text(ingreso_receta)
    print(f"Receta : {nombre_receta} creada")

def crear_categoria(ruta_principal):
    # Creo una variable donde almaceno la ruta de Recetas:
    ruta_de_recetas = Path(ruta_principal, "Recetas")
    nombre_categoria = input("Introduzca el nombre de la nueva categoría: ")

    # Instancio la ruta con el nombre creado a una variabla:
    ruta_categoria_creada = Path(ruta_de_recetas,Path(nombre_categoria))

    # creo la carpeta (categoria):
    ruta_categoria_creada.mkdir()
    print(f"Categoría : {nombre_categoria} creada")

def eliminar_receta(ruta_principal):
    # Creo una variable donde almaceno la ruta de Recetas:
    ruta_de_recetas = Path(ruta_principal, "Recetas")

    # Recorro la ruta de recetas mostrando el índice y nombre de subcarpetas:
    for indice, fichero in enumerate(ruta_de_recetas.iterdir()):
        print(indice, fichero.name)
    seleccion = int(input("Seleccione una carpeta: "))

    # A partir de la selección de usuario me posiciono en la ruta especificada
    for indice, fichero in enumerate(ruta_de_recetas.iterdir()):
        if seleccion == indice:
            ruta_receta_seleccionada = Path(ruta_de_recetas, Path(fichero))
            break;

    # Muestro los archivos dentro de la carpeta seleccionada
    for indice, fichero in enumerate(ruta_receta_seleccionada.iterdir()):
        # muestro el indice y el nombre del archivo sin la extensión
        print(indice, fichero.stem)
    seleccion_archivo = int(input("Seleccione una archivo: "))

    # Recorro los archivos buscando la coincidencia con la seleccion del usuario
    for indice, fichero in enumerate(ruta_receta_seleccionada.iterdir()):
        if seleccion_archivo == indice:
            ruta_archivo_seleccionado = Path(ruta_receta_seleccionada, Path(fichero))
            # leo el archivo seleccionado
            print(f"Receta : {fichero} eliminado")
            ruta_archivo_seleccionado.unlink()
            break;

def eliminar_categoria(ruta_principal):
    # Creo una variable donde almaceno la ruta de Recetas:
    ruta_de_recetas = Path(ruta_principal, "Recetas")

    # Recorro la ruta de recetas mostrando el índice y nombre de subcarpetas:
    for indice, fichero in enumerate(ruta_de_recetas.iterdir()):
        print(indice, fichero.name)
    seleccion = int(input("Seleccione una categoría: "))

    # A partir de la selección de usuario me posiciono en la ruta especificada
    for indice, fichero in enumerate(ruta_de_recetas.iterdir()):
        if seleccion == indice:
            ruta_receta_seleccionada = Path(ruta_de_recetas, Path(fichero))
            shutil.rmtree(ruta_receta_seleccionada)
            print(f"Categoría : {fichero} eliminada")
            break;

ruta=bienvenida_ruta_principal()
opcion=menu()
while opcion!=6:
    match opcion:
        case 1:
            system('cls')
            leer_receta(ruta)
            pass
        case 2:
            system('cls')
            crear_receta(ruta)
            pass
        case 3:
            system('cls')
            crear_categoria(ruta)
            pass
        case 4:
            system('cls')
            eliminar_receta(ruta)
            pass
        case 5:
            system('cls')
            eliminar_categoria(ruta)
            pass
    input("Presione ENTER para continuar")
    system('cls')
    opcion=menu()



