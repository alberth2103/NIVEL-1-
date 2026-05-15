# Dibujar un triángulo rectángulo de asteriscos
N = int(input("Ingrese la base del triángulo (N): "))

print(f"\n📐 TRIÁNGULO RECTÁNGULO DE BASE {N}")
print("=" * 40)

# Bucle externo: controla las FILAS
for fila in range(1, N + 1):
    
    # Bucle interno: controla las COLUMNAS (asteriscos en cada fila)
    for columna in range(1, fila + 1):
        print("*", end="")  # end="" evita el salto de línea
    
    print()  # Salto de línea al terminar cada fila

print("=" * 40)
print("✅ Triángulo completado")


# 1. Solicitar la base del triángulo
# N = int(input("Ingrese la base del triángulo (N): "))
# N determina la altura y la base del triángulo
# Si N = 5, el triángulo tendrá 5 filas y la última fila tendrá 5 asteriscos
# 2. Bucle externo: controla las FILAS
# for fila in range(1, N + 1):
# fila representa el número de la fila actual (1, 2, 3, ..., N)
# Cada iteración del bucle externo dibuja una fila completa
# 3. Bucle interno: controla los ASTERISCOS en cada fila
# for columna in range(1, fila + 1):
# print("*", end="")
# columna va desde 1 hasta fila
# En la fila 1 → dibuja 1 asterisco
# En la fila 2 → dibuja 2 asteriscos
# 3 En la fila 3 → dibuja 3 asteriscos
# ... y así sucesivamente
# 4. Salto de línea al final de cada fila
# print()  # Salto de línea