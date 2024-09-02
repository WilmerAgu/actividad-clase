def agregar_libro(biblioteca):
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    año = int(input("Introduce el año de publicación del libro: "))
    
    biblioteca[titulo] = {"autor": autor, "año": año, "disponible": True}
    print(f"El libro '{titulo}' ha sido añadido a la biblioteca.")

def prestar_libro(biblioteca):
    titulo = input("Introduce el título del libro que quieres prestar: ")
    
    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f"El libro '{titulo}' ha sido prestado.")
        else:
            print(f"El libro '{titulo}' no está disponible.")
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def devolver_libro(biblioteca):
    titulo = input("Introduce el título del libro que quieres devolver: ")
    
    if titulo in biblioteca:
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f"El libro '{titulo}' ha sido devuelto y ahora está disponible.")
        else:
            print(f"El libro '{titulo}' ya estaba disponible.")
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def mostrar_libros(biblioteca):
    if not biblioteca:
        print("La biblioteca está vacía.")
    else:
        for titulo, info in biblioteca.items():
            autor = info["autor"]
            año = info["año"]
            disponible = "Disponible" if info["disponible"] else "No disponible"
            print(f"Título: {titulo}\nAutor: {autor}\nAño: {año}\nDisponibilidad: {disponible}\n")

def mostrar_libros_por_año(biblioteca, año):
    encontrados = False
    for titulo, info in biblioteca.items():
        if info["año"] == año:
            encontrados = True
            autor = info["autor"]
            disponible = "Disponible" if info["disponible"] else "No disponible"
            print(f"Título: {titulo}\nAutor: {autor}\nAño: {año}\nDisponibilidad: {disponible}\n")
    
    if not encontrados:
        print(f"No se encontraron libros publicados en el año {año}.\n")

def menu():
    biblioteca = {
        "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
        "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
        "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
    }
    
    while True:
        print("Menú de la Biblioteca:")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Ver libros por año de publicación")
        print("6. Salir del programa")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            prestar_libro(biblioteca)
        elif opcion == "3":
            devolver_libro(biblioteca)
        elif opcion == "4":
            mostrar_libros(biblioteca)
        elif opcion == "5":
            año = int(input("Introduce el año de publicación: "))
            mostrar_libros_por_año(biblioteca, año)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.\n")

menu()
