# Calcular la suma de los números del 1 al 50
suma_total = 0  # Inicializamos el acumulador

for numero in range(1, 51):
    suma_total = suma_total + numero  # Acumulamos cada número

print(f"La suma de los números del 1 al 50 es: {suma_total}")


# 1-suma_total = 0
# Un acumulador es una variable que guarda resultados parciales
# Se inicializa en 0 porque empezamos sin ninguna suma
#En cada iteración, iremos agregando (acumulando) nuevos valores

# 2-El bucle for con range()
python
# for numero in range(1, 51):
# range(1, 51) genera: 1, 2, 3, ..., 49, 50
# La variable numero toma cada valor del 1 al 50, uno por uno

# 3-La operación de acumulación
# suma_total = suma_total + numero
# Toma el valor actual del acumulador
#Le suma el nuevo número
# Guarda el resultado en el acumulador
