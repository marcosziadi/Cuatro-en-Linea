
def tablerovacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


def soltarfichaencolumna(tablero, secuencia):
    validez = validarcolumna(secuencia)
    if validez:
     for row in range(5, 0, -1):
         for c in range(len(secuencia)):
                if c % 2 == 0:
                    if tablero[row][secuencia[c] - 1] == 0:
                        tablero[row][secuencia[c] - 1] = 1
                else:
                    if tablero[row][secuencia[c] - 1] == 0:
                     tablero[row][secuencia[c] - 1] = 2
    return


def validarcolumna(secuencia):
    a = 0
    b = 0
    for c in range(len(secuencia)):
        if 8 > secuencia[c] > 0:
            a += 1
        else:
            b += 1
    if len(secuencia) == (a - b):
        return True
    else:
        return False


def imprimirtablero(tablero, secuencia):
    validez = validarcolumna(secuencia)
    if validez:
        for row in tablero:
            print(row)
    else:
        print("La secuencia no es valida")


def contenidocolumna(nrocol, tablero):
    columna = []
    for row in tablero:
        celda = row[nrocol - 1]
        columna.append(celda)
    return columna


secuencia = [1, 2, 3, 4, 1, 2, 3, 4]
tablero = tablerovacio()
soltarfichaencolumna(tablero, secuencia)
imprimirtablero(tablero, secuencia)
print(contenidocolumna(2, tablero))

