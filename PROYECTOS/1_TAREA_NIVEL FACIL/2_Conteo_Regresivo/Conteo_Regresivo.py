# Cuenta regresiva desde N hasta 0
N = int(input("Ingrese el número inicial para la cuenta regresiva: "))

print(f"\n¡CUENTA REGRESIVA DESDE {N} HASTA 0!")
print("=" * 40)

while N >= 0:
    print(f"Número: {N}")
    N = N - 1  # Decremento en 1

print("=" * 40)
print("¡DESPEGUE! 🚀")

# Entrada del usuario
# N = int(input("Ingrese el número inicial para la cuenta regresiva: "))
# input() captura el valor ingresado por el usuario (como texto)
# int() convierte ese texto a un número entero
# La variable N almacena el número desde donde comenzará la cuenta regresiva
# Estructura del bucle while