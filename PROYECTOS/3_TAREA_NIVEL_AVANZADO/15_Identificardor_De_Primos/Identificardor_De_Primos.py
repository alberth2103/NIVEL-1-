# Verificar si un número es primo
numero = int(input("Ingrese un número para verificar si es primo: "))

# Los números menores o iguales a 1 no son primos
if numero <= 1:
    print(f"\n❌ {numero} NO es primo (debe ser mayor que 1)")
else:
    # Verificar si tiene algún divisor entre 2 y numero-1
    for divisor in range(2, numero):
        if numero % divisor == 0:
            print(f"\n❌ {numero} NO es primo")
            print(f"   Es divisible por {divisor} ({numero} ÷ {divisor} = {numero // divisor})")
            break  # Salir del bucle porque ya encontramos un divisor
    else:
        # Este bloque se ejecuta si el bucle NO encontró ningún break
        print(f"\n✅ {numero} SÍ es primo")
        print(f"   Solo es divisible por 1 y por sí mismo")



# 1. ¿Qué es un número primo?
# Un número primo es aquel mayor que 1 que solo es divisible por 1 y por sí mismo.
# Ejemplos:
# 2, 3, 5, 7, 11, 13, 17, 19, 23... son primos
# 4, 6, 8, 9, 10, 12, 14, 15... NO son primos
# 2. Caso especial: números ≤ 1
# if numero <= 1:
#  print(f"\n❌ {numero} NO es primo (debe ser mayor que 1)")
# El 1 NO es primo por definición
# Los números negativos y el 0 tampoco son primos
# 3. El bucle for para buscar divisores
# for divisor in range(2, numero):
# range(2, numero) genera números desde 2 hasta numero-1
# Probamos cada posible divisor
# Ejemplo: Si numero = 7, probamos: 2, 3, 4, 5, 6
# 4. Verificar si es divisible
# if numero % divisor == 0:
# Si el residuo es 0, encontramos un divisor
# Eso significa que NO es primo
# 5. El break al encontrar divisor
# break
# Salimos del bucle porque ya sabemos que no es primo
# No tiene sentido seguir buscando más divisores
# 6. El bloque else del bucle (LA MAGIA)         