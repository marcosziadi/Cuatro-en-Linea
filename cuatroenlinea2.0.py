#Cuatro En Linea Juego AAT
def tablerovacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


def soltarfichaencolumna(ficha, columna, tablero):
    for row in range(6, 0, -1):
        if tablero[row - 1][int(columna) - 1] == 0:
            tablero[row - 1][int(columna) - 1] = ficha
            return


def tirovalido(columna):
    if int(columna) > 7 or int(columna) < 1:
        return False
    else:
        return True


def juego(secuencia):
    for i, a in enumerate(secuencia):
        if i % 2 == 0:
          ficha = 1
        else:
          ficha = 2

#        columna = input("\nInsertar Numero de Columna: ")

        if tirovalido(a):
            soltarfichaencolumna(ficha, a, tablero)
            for row in tablero:
                print(" |", end="")
                for col in row:
                    if col == 0:
                        print("   ", end="")
                    else:
                        print(f"  {col}", end='')
                print(" |")
                print("\n")
            print(" +---------------------+")
        else:
            print("Valor de Columna Inválido")
            secuencia_input = input("Ingrese los valores de la secuencia: ")
            secuencia = []
            for item in secuencia_input.split(" "):
                secuencia.append(int(item))
                juego(secuencia)
            break


def contenidoFila(fila, tablero):
    imprimir = []
    abc = 6 - int(fila)
    for a in range(0, 7, +1):
        celda = tablero[abc][a]
        imprimir.append(celda)
    return imprimir


def contenidoCol(columna, tablero):
    imprimir = []
    for a in range(5, -1, -1):
        celda = tablero[a][int(columna) - 1]
        imprimir.append(celda)
    return imprimir


tablero = tablerovacio()
for row in tablero:
    print(" |", end="")
    for col in row:
        if col == 0:
            print("   ", end="")
        else:
            print(f" {col}  ", end='')
    print("|")
    print("\n")
print(" +---------------------+")
secuencia_input = input("Ingrese los valores de la secuencia: ")
secuencia = []
for item in secuencia_input.split(" "):
    secuencia.append(int(item))
print(secuencia)
juego(secuencia)
fila = input("\nNro de Fila que desea Imprimir: ")
imprimir = contenidoFila(fila, tablero)
print(imprimir)
columna = input("\nNro de Columna que desea Imprimir: ")
impri = contenidoCol(columna, tablero)
print(impri)

