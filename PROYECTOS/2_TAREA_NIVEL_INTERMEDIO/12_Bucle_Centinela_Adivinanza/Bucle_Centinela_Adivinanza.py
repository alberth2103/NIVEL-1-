# Mostrar los primeros N términos de Fibonacci
n = int(input("¿Cuántos términos de Fibonacci quieres ver? "))

# Valores iniciales
a, b = 0, 1  # Asignación múltiple: a = 0, b = 1

print(f"\n📊 LOS PRIMEROS {n} TÉRMINOS DE FIBONACCI:")
print("=" * 40)

for i in range(n):
    print(f"{i+1}: {a}")
    a, b = b, a + b  # Asignación múltiple: a = b, b = a + b

print("=" * 40)

# 1. Solicitar el número de términos
# n = int(input("¿Cuántos términos de Fibonacci quieres ver? "))
# El usuario indica cuántos números de la secuencia quiere ver
# Ejemplo: si ingresa 10, mostrará los primeros 10 términos
# 2. Asignación múltiple (clave del algoritmo)
# a, b = 0, 1
# Asignación múltiple asigna valores a varias variables en una sola línea
# Es equivalente a:
# a = 0
# b = 1
# a representa el término actual
# b representa el siguiente término
# 3. El bucle for
# for i in range(n):
# Itera n veces (una por cada término que queremos mostrar)
# i toma valores de 0 a n-1
# 4. Mostrar el término actual
# print(f"{i+1}: {a}")
# i+1 es el número de término (1, 2, 3, ...)
# a es el valor de Fibonacci en esa posición
# 5. La magia de la asignación múltiple
# a, b = b, a + b
# Esta línea es el corazón del algoritmo
# Se evalúan primero todos los valores del lado derecho
# Luego se asignan a las variables del lado izquierdo
# Es equivalente a (pero más eficiente):
# temp = a
# a = b
# b = temp + b
# ¿Qué pasa internamente? (Ejemplo con n = 7)