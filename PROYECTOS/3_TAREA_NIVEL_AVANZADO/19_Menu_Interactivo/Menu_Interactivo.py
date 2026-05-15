# Menú en consola con 3 operaciones + salida
# Se usa un bucle while para repetir el menú hasta que el usuario elija salir

while True:
    # Mostrar el menú de opciones
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir del programa")
    
    # Solicitar la opción al usuario
    opcion = input("Elige una opción (1-4): ")
    
    # Evaluar la opción con estructura if-elif-else
    if opcion == "1":
        print("\n--- SUMA ---")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de {num1} + {num2} es: {resultado}")
    
    elif opcion == "2":
        print("\n--- RESTA ---")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de {num1} - {num2} es: {resultado}")
    
    elif opcion == "3":
        print("\n--- MULTIPLICACIÓN ---")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de {num1} * {num2} es: {resultado}")
    
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Rompe el bucle while y termina el programa
    
    else:
        print("Opción no válida. Por favor elige un número entre 1 y 4.")


# Bucle while True: Hace que el menú se repita indefinidamente hasta que se ejecute break.
# Estructura if-elif-else:
# if opcion == "1": Maneja la suma.
# elif opcion == "2": Maneja la resta.
# elif opcion == "3": Maneja la multiplicación.
# elif opcion == "4": Sale del bucle con break.
# else: Captura cualquier entrada no válida (números fuera de 1-4 o texto).
# Entrada de datos: Se usa input() para leer la opción y los números. float() convierte a número decimal para permitir operaciones con decimales.
# Salida formateada: Se usa f-strings para mostrar los resultados claramente.
# Ejemplo de ejecución:
# --- MENÚ PRINCIPAL ---
# 1. Sumar dos números
# 2. Restar dos números
# 3. Multiplicar dos números
# 4. Salir del programa
# Elige una opción (1-4): 1
#--- SUMA ---
# Ingresa el primer número: 5
# Ingresa el segundo número: 3
# l resultado de 5.0 + 3.0 es: 8.0
# --- MENÚ PRINCIPAL ---
# 1. Sumar dos números
# 2. Restar dos números
# 3. Multiplicar dos números
# 4. Salir del programa
# Elige una opción (1-4): 4
# Saliendo del programa. ¡Hasta luego!