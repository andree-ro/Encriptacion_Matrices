import numpy as np


def matrix_invert(matrix):
    # Get the dimensions of the matrix
    n = len(matrix)
    m = len(matrix[0])

    # Check if the matrix is square
    if n != m:
        return 'Error'

    # Create an augmented matrix [matrix | identity]
    augmented_matrix = [row + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]

    # Apply Gauss-Jordan elimination
    for i in range(n):
        # Find the pivot row
        pivot_row = max(range(i, n), key=lambda x: abs(augmented_matrix[x][i]))

        # Swap the current row with the pivot row
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]

        # Scale the pivot row to make the pivot element equal to 1
        pivot = augmented_matrix[i][i]
        augmented_matrix[i] = [element / pivot for element in augmented_matrix[i]]

        # Eliminate other rows
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [row_j - factor * row_i for row_i, row_j in
                                       zip(augmented_matrix[i], augmented_matrix[j])]

    # Extract the inverse matrix from the augmented matrix
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix


def texto_numeros(frase):
    letras = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
        "L": 12, "M": 13, "N": 14, "Ñ": 15, "O": 16, "P": 17, "Q": 18, "R": 19, "S": 20, "T": 21,
        "U": 22, "V": 23, "W": 24, "X": 25, "Y": 26, "Z": 27, " ": 28
    }

    matrixCifrar = [[], [], []]

    numeros = [letras[letra] for letra in frase]

    for i, num in enumerate(numeros):
        if i % 3 == 0:
            matrixCifrar[0].append(num)
        elif i % 3 == 1:
            matrixCifrar[1].append(num)
        else:
            matrixCifrar[2].append(num)

    return matrixCifrar


def clave_matriz(columnas):
    matriz_clave = []
    for i in range(3):
        matriz_fila = []
        for j in range(columnas):
            dato = int(input(f"Ingrese el dato que está en {i + 1}, {j + 1}: "))
            matriz_fila.append(dato)
        matriz_clave.append(matriz_fila)
    return matriz_clave


columnas = int(input("Ingrese cuántas columnas tendrá la clave: "))
matriz_clave = clave_matriz(columnas)
frase = input("Ingrese el texto a encriptar: ")

while True:
    A = np.array(matriz_clave)
    B = np.array(texto_numeros(frase))
    r = np.matmul(A, B)

    print("Menu")
    print("1. Encriptar.")
    print("2. Desencriptar.")
    print("3. Salir.")
    opcion = int(input("Ingrese la opción que desea: "))

    if opcion == 1:
        print(r)

    elif opcion == 2:
        invert = matrix_invert(matriz_clave)
        if invert == "Error":
            print("La matriz clave no tiene inversa.")
        else:
            A2 = np.array(invert)
            B2 = np.array(r)
            r2 = np.matmul(A2, B2)
            print(r2)

    elif opcion == 3:
        break