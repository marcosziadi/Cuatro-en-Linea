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
    for a in secuencia:
        if a % 2 == 0:
          ficha = 1
        else:
          ficha = 2

        columna = input("\nInsertar Numero de Columna: ")

        if tirovalido(columna):
            soltarfichaencolumna(ficha, columna, tablero)
            for row in tablero:
                print(row)
        else:
            print("Valor de Columna Inválido")
            break

def contenidoFila(fila, tablero):
    imprimir = []
    abc = 6 - int(fila)
    for a in range(0, 7, +1):
        celda = tablero[abc][a]
        imprimir.append(celda)
    return imprimir


tablero = tablerovacio()
for row in tablero:
       print(row)
secuencia = [0,1,2,3,4]
juego(secuencia)
fila = input("Nro de Fila que desea Imprimir: ")
imprimir = contenidoFila(fila, tablero)
print(imprimir)

