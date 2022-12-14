from datos import fichas

def imprimir_tablero(fichas): # Imprime el tablero de ajedrez
    print("  A B C D E F G H")
    for i in range(8):
        print(i+1, end=" ") # Imprime el número de la fila
        for j in range(8):
            print(fichas[i][j], end=" ") # Imprime la ficha
        print()

def guardar_tablero(fichas, nombre): # Guarda el tablero en un archivo
    nombretxt = "movimientos/" + nombre + ".txt" # Nombre del archivos
    with open (nombretxt, 'a', encoding = 'utf-8') as archivo: # Abre el archivo
        archivo.writelines('\n')
        for i in range(8): # Recorre las filas
            archivo.writelines(fichas[i]) # Escribe la fila
        archivo.close()

def inicio(fichas): # Menú de inicio
    print("Bienvenido al ajedrez")
    print("1. Jugar")
    print("2. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        imprimir_tablero(fichas)
        juego(fichas)
    elif opcion == 2:
        print("Gracias por jugar")
    else:
        print("Opción no válida")
        inicio()


def movimiento(fichas): # Movimiento de las fichas
    imprimir_tablero(fichas)
    columnas = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    print("El formato establecido sería el siguiente: A1 (Columna y fila)")
    columna = input("Ingrese la columna de la ficha: ")
    fila = int(input("Ingrese la fila de la ficha: "))
    columna = columnas[columna]
    if fila > 8 or columna > 8:
        print("Opción no válida")
        movimiento(fichas)
    elif 0<fila<9 and 0<columna<9:
        ficha = fichas[fila-1][columna-1] # Ficha a mover
        columna_nueva = input("Ingrese la columna a la que desea mover la ficha: ")
        fila_nueva = int(input("Ingrese la fila a la que desea mover la ficha: "))
        columna_nueva = columnas[columna_nueva]
        if fichas[fila_nueva-1][columna_nueva-1] == " ": # Si la posición a la que se quiere mover está vacía
            fichas[fila_nueva-1][columna_nueva-1] = ficha
            fichas[fila-1][columna-1] = ' '
            imprimir_tablero(fichas)
            juego(fichas)
        elif fichas[fila_nueva][columna_nueva] != " ": # Si la posición a la que se quiere mover está ocupada
            print("No puede mover la ficha a esa posición")
            movimiento(fichas)
        else:
            print("No puede mover la ficha a esa posición")
            movimiento(fichas)
    else:
        print("No puede mover la ficha a esa posición")
        movimiento(fichas)


def juego(fichas): # Juego
    pregunta = int(input("¿Desea guardar este tablero? 1. Si 2. No: ")) # Desea guardar el tablero en un archivo
    if pregunta == 1:
        nombre = input("Ingrese el nombre del archivo: ")
        guardar_tablero(fichas, nombre)
        pregunta2 = int(input("¿Desea hacer movimientos? 1. Si 2. No: "))
        if pregunta2 == 1:
            movimiento(fichas)
        elif pregunta2 == 2:
            print("Gracias por jugar")
    elif pregunta == 2:
        movimiento(fichas)
    else:
        print("Opción no válida")
        inicio(fichas)
