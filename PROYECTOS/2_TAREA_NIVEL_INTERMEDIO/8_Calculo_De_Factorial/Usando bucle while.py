# Calcular factorial con bucle while
numero = int(input("Ingrese un número para calcular su factorial: "))

factorial = 1
contador = 1

while contador <= numero:
    factorial = factorial * contador
    contador = contador + 1

print(f"✅ El factorial de {numero}! es: {factorial}")