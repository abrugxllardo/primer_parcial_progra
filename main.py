#Abril gallardo
from funciones import * 
seguir = "si"

while seguir == "si":
    match menu():
        case "A":
            lista = leer_archivo(get_path_actual("movies.csv"))
            imprimir_lista(lista)        
        case "B":
            for pelicula in lista:
                asignar_rating(pelicula)
                asignar_genero(pelicula)
            imprimir_lista(lista)
        case "C":
            lista_ordenada = ordenar_peliculas_genero_rating(lista)
            imprimir_lista(lista_ordenada)
        case "D":
            genero = input("Ingrese el genero que desea: ")
            lista_generos = ["drama", "comedia", "accion", "terror"]
            while genero not in lista_generos:
                genero = input("Error, ingrese el genero que desea: ")
            filtrar_por_genero(lista, genero)
        case "E":
            lista_ordenada = ordenar_peliculas_genero_rating(lista)
            imprimir_lista(lista_ordenada)
        case "F":
            lista_mejor_rating = mejor_rating(lista)
            imprimir_lista(lista_mejor_rating)
        case "G":
            lista_mejor_rating = mejor_rating(lista)
            cargar_lista_json(lista_mejor_rating)
        case "H":
            if pedirConfirmacion("Confirmar salida si/no: "):
                seguir = "no"
            continue
    pausar()