def ordenar_fila(matriz, fila):
    fila_a_ordenar = matriz[fila].copy()

    for i in range(len(fila_a_ordenar)):
        min_idx = i
        for j in range(i + 1, len(fila_a_ordenar)):
            if fila_a_ordenar[j] < fila_a_ordenar[min_idx]:
                min_idx = j
        fila_a_ordenar[i], fila_a_ordenar[min_idx] = fila_a_ordenar[min_idx], fila_a_ordenar[i]

    matriz[fila] = fila_a_ordenar


def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


matriz = [
    [9, 3, 7],
    [4, 1, 5],
    [6, 2, 8]
]

print("Matriz original:")
imprimir_matriz(matriz)
print()

ordenar_fila(matriz, 2)

print("Matriz con la fila ordenada:")
imprimir_matriz(matriz)