# Calcular factorial con bucle while
numero = int(input("Ingrese un número para calcular su factorial: "))

factorial = 1
contador = 1

while contador <= numero:
    factorial = factorial * contador
    contador = contador + 1

print(f"✅ El factorial de {numero}! es: {factorial}")


# Solicitar el número al usuario
# numero = int(input("Ingrese un número para calcular su factorial: "))
# input() captura el valor ingresado
# int() convierte el texto a número entero
# 2- Inicializar el acumulador
# factorial = 1
# El factorial comienza en 1 (no en 0 porque multiplicar por 0 daría 0)
# 1 es el elemento neutro de la multiplicación
# 3. El bucle (versión for)
# for i in range(1, numero + 1):
# factorial = factorial * i
# range(1, numero + 1) genera números desde 1 hasta numero
# En cada iteración, multiplicamos el factorial actual por el número i
# 4. Mostrar el resultado
# print(f"✅ El factorial de {numero}! es: {factorial}")