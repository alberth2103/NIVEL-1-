# Definir una matriz 3x3 (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicializar el acumulador de la suma
suma_total = 0

# Recorrer cada fila de la matriz con un bucle for externo
for i in range(len(matriz)):  # i representa el índice de la fila (0, 1, 2)
    # Recorrer cada columna de la fila actual con un bucle for interno
    for j in range(len(matriz[i])):  # j representa el índice de la columna (0, 1, 2)
        # Acceder al elemento en la posición [fila][columna] y sumarlo
        suma_total += matriz[i][j]
        # Mostrar el proceso paso a paso (opcional, para entender mejor)
        print(f"Sumando elemento en posición [{i}][{j}] = {matriz[i][j]} - Acumulado parcial: {suma_total}")

# Mostrar el resultado final
print(f"\nLa suma total de todos los elementos de la matriz es: {suma_total}")


# Estructura de la matriz 3x3
# matriz = [
#    [1, 2, 3],   # Fila 0 (índice 0)
#    [4, 5, 6],   # Fila 1 (índice 1)
#    [7, 8, 9]    # Fila 2 (índice 2)
# 2. Bucle for externo (recorre filas)
# for i in range(len(matriz)) → len(matriz) = 3 (cantidad de filas)
# i toma los valores: 0, 1, 2
# Cada valor de i representa una fila completa
# 3. Bucle for interno (recorre columnas)
# for j in range(len(matriz[i])) → len(matriz[i]) = 3 (cantidad de columnas por fila)
# j toma los valores: 0, 1, 2
# Cada valor de j representa una columna dentro de la fila actual
# 4. Acceso a cada elemento
# matriz[i][j] accede al valor en la fila i y columna j
# Ejemplo: matriz[0][0] = 1, matriz[0][1] = 2, matriz[2][2] = 9
# 5. Acumulación de la suma
# suma_total += matriz[i][j] es equivalente a suma_total = suma_total + matriz[i][j]