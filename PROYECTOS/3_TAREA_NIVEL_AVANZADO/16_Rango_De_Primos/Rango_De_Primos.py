# Imprimir todos los números primos del 1 a N
N = int(input("Ingrese el límite superior (N): "))

print(f"\n📊 NÚMEROS PRIMOS DEL 1 AL {N}")
print("=" * 40)

# Bucle externo: recorre cada número del 1 al N
for numero in range(1, N + 1):
    
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        continue  # Saltar este número
    
    # Bucle interno: verifica si el número es primo
    es_primo = True  # Suponemos que es primo hasta encontrar divisor
    
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False  # Encontramos un divisor, NO es primo
            break  # Salir del bucle interno
    
    # Si es primo, lo imprimimos
    if es_primo:
        print(f"  ✅ {numero} es primo")

print("=" * 40)
print(f"✅ Se mostraron todos los primos hasta {N}")

# 1. Bucle externo: Recorrer cada número
# for numero in range(1, N + 1):
# Este bucle recorre todos los números desde 1 hasta N
# numero toma los valores: 1, 2, 3, 4, 5, ..., N
# 2. Saltar números no candidatos
# if numero <= 1:
# continue
# Los números ≤ 1 no son primos (por definición)
# continue salta a la siguiente iteración del bucle externo
# 3. Bucle interno: Verificar si es primo
# for divisor in range(2, numero):
# if numero % divisor == 0:
# es_primo = False
# break
# Este bucle prueba todos los divisores potenciales
# Si encuentra un divisor exacto, el número NO es primo
# break sale del bucle interno (ya sabemos que no es primo)
# 4. Imprimir si es primo
# if es_primo:
# print(f"  ✅ {numero} es primo")