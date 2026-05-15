# Calcular el MCD de dos números usando el Algoritmo de Euclides
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Guardar valores originales para mostrar al final
original1 = num1
original2 = num2

print(f"\n🔍 CALCULANDO EL MCD DE {original1} Y {original2}")
print("=" * 50)
print(f"Usando el Algoritmo de Euclides:")
print("-" * 50)

# Algoritmo de Euclides
while num2 != 0:
    residuo = num1 % num2
    print(f"{num1} ÷ {num2} = {num1 // num2} , residuo = {residuo}")
    num1 = num2
    num2 = residuo
    print(f"  → Nuevos valores: a = {num1}, b = {num2}")

print("-" * 50)
print(f"✅ El MCD de {original1} y {original2} es: {num1}")
print("=" * 50)


# 1. ¿Qué es el MCD?
# El Máximo Común Divisor es el número más grande que divide exactamente a dos números.
# Ejemplo: MCD(12, 18) = 6 porque:
# Divisores de 12: 1, 2, 3, 4, 6, 12
# Divisores de 18: 1, 2, 3, 6, 9, 18
# El mayor común: 6
# 2. El Algoritmo de Euclides
# Es un método eficiente para encontrar el MCD basado en la propiedad:
# text
# MCD(a, b) = MCD(b, a % b)
# Pasos:
# Dividir el número mayor entre el menor
# Reemplazar el mayor con el menor
# Reemplazar el menor con el residuo
# Repetir hasta que el residuo sea 0
# El último divisor no cero es el MCD
# 3. La lógica del bucle while
# while num2 != 0:
# Mientras el segundo número NO sea cero, continuamos
# Cuando num2 llega a 0, num1 contiene el MCD
# 4. Calcular el residuo
# residuo = num1 % num2
# % es el operador módulo (residuo de la división)
# Ejemplo: 18 % 12 = 6
# 5. Actualizar los valores
# num1 = num2  # El divisor se convierte en nuevo dividendo
#num2 = residuo  # El residuo se convierte en nuevo divisor