#Abril gallardo
import random
import json
def menu():
    limpiar_pantalla()
    print(f"{"** PELICULAS **":^50s}")
    print("A- Imprimir lista de peliculas")
    print("B- Asignar rating y genero a cada pelicula")
    print("C- Ordenar las peliculas por genero y rating")
    print("D- Crear archivo filtrando las peliculas por genero")
    print("E- Mostrar la pelicula con mejor rating")
    print("F- Guardar un listado de mejor rating a peor en archivo json")
    print("H- Salir del programa")
    return ingresar_opcion()

def limpiar_pantalla():
    """Limpia pantalla por cada iteracion
    """
    import os
    os.system("cls")

def pausar():
    """Pausa el programa en cada iteracion
    """
    import os
    os.system("pause")

def ingresar_opcion()->str:
    """pide al usuario que ingrese la opcion

    Returns:
        str: retorna la opcion querida
    """
    opcion = input("Ingrese una opcion: ").upper()

    while opcion not in "ABCDEFGH":
        opcion = input("Error, ingrese una opcion: ").upper()

    return opcion

def pedirConfirmacion(mensaje:str)->str:
    """Confirma la salida del programa

    Args:
        mensaje (str): mensaje hacia el usuario

    Returns:
        str: retorna la respuesta del usuario
    """
    rta = input(mensaje).lower()
    return rta == "si"

def get_path_actual(nombre_archivo):
    """buscar el nombre der archivo en el directorio

    Args:
        nombre_archivo (_type_): nombre de archivo a buscar

    Returns:
        _type_: retorna la ruta completa del archivo con el directorio actual
    """
    import os
    directoria_actual = os.path.dirname(__file__)
    return  os.path.join(directoria_actual, nombre_archivo)

def leer_archivo(nombre_archivo)-> list:
    """se abre el archivo para poder usar la info de dentro

    Args:
        nombre_archivo (_type_): nombre de archivo a buscar

    Returns:
        list: una lista de diccionarios con todos los datos que tiene dentro
    """
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
        
        for linea in archivo.readlines():
            pelicula = {}
            linea = linea.strip("\n").split(",")
            print(linea)
            id, titulo, genero, rating = linea #unpacking
            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = float(rating)
            lista.append(pelicula)
    return lista 

lista = leer_archivo(get_path_actual("movies.csv"))

def imprimir_lista(lista:list):
    """imprime cada valor de la key que esta en la lista

    Args:
        lista (list): lista a recorrer
    """
    print("                      *** PELICULAS ***       ")
    print("ID      TITULO                            GENERO         RATING")
    for dato in lista:
        print(f"{dato["id"]:<3}     {dato["titulo"]:<30}     {dato["genero"]:<10}     {dato["rating"]}")


def asignar_rating(dato)-> int:
    """asiga un valor al dato aleatoriamente del 1 al 10

    Args:
        dato (_type_): dato al que se quiere darle el valor

    Returns:
        _type_: retorna el valor asignado
    """
    dato["rating"] = round(random.randint(10, 100) / 10, 1)
    return dato

def asignar_genero(dato) ->str:
    """asiga un genero aleatoriamente entre los cuato generos

    Args:
        dato (_type_): dato al que se quiere darle el genero

    Returns:
        _type_: retorna el genero asignado
    """
    generos = ["drama", "comedia", "accion", "terror"]
    dato["genero"] = random.choice(generos)
    return dato
    
for pelicula in lista:
    asignar_rating(pelicula)
    asignar_genero(pelicula)


def cargar_personas(lista:list, nombre_archivo:str):
    """crea un archivo csv y le carga la lista con los datos

    Args:
        lista (list): lista a cargar el archivo
        nombre_archivo (str): nombre del archivo que va a ser creado
    """
    with open(get_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            l = []
            values = list(persona.values())
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)

def swapLista(lista:list, i :int, j:int):
    """intercambia los elementos en una lista

    Args:
        lista (list): La lista en la que se genera el intercambio.
        i (int):  El indice del primer elemento a intercambiar.
        j (int): El indice del segundo elemento a intercambiar.
    """
    
    aux = lista[i]
    lista[i], lista[j] = lista[j], aux

def ordenar_peliculas_genero_rating(lista:list)-> list:
    """ordena una lista segun lo pedido, es este caso genero y legajo

    Args:
        lista (list): lista con los datos a ordenar

    Returns:
        _type_: retorna la lista ordenada
    """
    cant = len(lista)
    for i in range(cant - 1):
        for j in range(i + 1, cant):
            if lista[i]["genero"] == lista[j]["genero"]:
                if lista[i]["rating"] < lista[j]["rating"]:
                    swapLista(lista, i, j)
            elif lista[i]["genero"] < lista[j]["genero"]:
                swapLista(lista, i, j)
    return lista

def mejor_rating(lista:list)-> list:
    """ordena la lista del mejor rating al peor

    Args:
        lista (list): lista a ordenar

    Returns:
        _type_: retorna la lista ordenada
    """
    cant = len(lista)
    for i in range(cant - 1):
        for j in range(i + 1, cant):
            if lista[i]["rating"] < lista[j]["rating"]:
                swapLista(lista, i, j)
    return lista


def cargar_lista_json( lista:list):
    """crea un archivo json y le carga una lista

    Args:
        lista (list): lista que se cargo al archivo
    """
    with open("mejor_rating.json", "w", encoding= "utf_8") as archivo:
        json.dump(lista, archivo, indent=4)


def filtrar_por_genero(lista:list, genero:str):
    """
    se pide un genero, lo filtra de la lista y lo carga en un archivo csv

    Args:
        lista (list): lista que se carga al archivo
        genero (str): genero a buscar
    """
    nombre_archivo = f"{genero}.csv"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        encabezados = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezados)
        for pelicula in lista:
            if pelicula["genero"] == genero:
                l = []
                values = list(pelicula.values())
                for value in values:
                    if isinstance(value, int):
                        l.append(str(value))
                    elif isinstance(value, float):
                        l.append(str(value))
                    else:
                        l.append(value)
                linea = ",".join(l) + "\n"
                archivo.write(linea)




