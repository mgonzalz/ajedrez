from datos import fichas

def imprimir_tablero(fichas): # Imprime el tablero de ajedrez
    print("  1 2 3 4 5 6 7 8")
    for i in range(8):
        print(i+1, end=" ") # Imprime el número de la fila
        for j in range(8):
            print(fichas[i][j], end=" ") # Imprime la ficha
        print()

def guardar_tablero(fichas, nombre): # Guarda el tablero en un archivo
    nombretxt = nombre + ".txt"
    with open (nombretxt, 'a') as archivo:
        for i in range(8):
            archivo.writelines(fichas[i]) # Escribe la fila
        archivo.close()
    movimiento(fichas)

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
    fila = int(input("Ingrese la fila de la ficha: "))
    columna = int(input("Ingrese la columna de la ficha: "))
    if fila > 8 or columna > 8:
        print("Opción no válida")
        movimiento(fichas)
    else:
        ficha = fichas[fila-1][columna-1] # Ficha a mover
        fila_nueva = int(input("Ingrese la fila a la que desea mover la ficha: "))
        columna_nueva = int(input("Ingrese la columna a la que desea mover la ficha: "))
        if fichas[fila_nueva-1][columna_nueva-1] == " ": # Si la posición a la que se quiere mover está vacía
            fichas[fila_nueva-1][columna_nueva-1] = ficha
            fichas[fila-1][columna-1] = ' '
            imprimir_tablero(fichas)
            juego(fichas)
        elif fichas[fila_nueva][columna_nueva] != " ": # Si la posición a la que se quiere mover está ocupada
            print("No puede mover la ficha a esa posición")
            movimiento(fichas)

def juego(fichas): # Juego
    pregunta = int(input("¿Desea guardar este tablero? 1. Si 2. No: ")) # Desea guardar el tablero en un archivo
    if pregunta == 1:
        nombre = input("Ingrese el nombre del archivo: ")
        guardar_tablero(fichas, nombre)
    elif pregunta == 2:
        movimiento(fichas)
    else:
        print("Opción no válida")
        inicio(fichas)

if __name__ == '__main__':
    inicio(fichas)
