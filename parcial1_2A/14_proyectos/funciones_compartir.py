peliculas = []

def esperar_confirmacion():
    input("Presione Enter para continuar...")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar película")
    print("2. Eliminar película")
    print("3. Actualizar película")
    print("4. Consultar película")
    print("5. Buscar películas")
    print("6. Actualizar películas")
    print("7. Salir")

def agregar_pelicula(nombre):
    peliculas.append(nombre)
    print(f'Película "{nombre}" agregada.')

def remover_pelicula(nombre):
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f'Película "{nombre}" eliminada.')
    else:
        print(f'La película "{nombre}" no se encuentra en la lista.')

def consultar_peliculas():
    if peliculas:
        print("Lista de películas:")
        for pelicula in peliculas:
            print(f'- {pelicula}')
    else:
        print("No hay películas en la lista.")

def buscar_peliculas():
    buscar = input("Ingrese el nombre de la película que busca: ")
    if buscar in peliculas:
        print(f'La película "{buscar}" se encuentra en la lista.')
    else:
        print(f'La película "{buscar}" no se encuentra en la lista.')

def vaciar_peliculas():
    peliculas.clear()
    print("La lista de películas ha sido vaciada.")

def actualizar_peliculas():
    nombre = input("Ingrese el nombre de la película que desea actualizar: ")
    if nombre in peliculas:
        nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
        peliculas[peliculas.index(nombre)] = nuevo_nombre
        print(f'La película "{nombre}" ha sido actualizada a "{nuevo_nombre}".')
    else:
        print(f'La película "{nombre}" no se encuentra en la lista.')
