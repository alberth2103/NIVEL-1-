# Cuenta progresiva desde 0 hasta N
N = int(input("Ingrese el número límite para la cuenta progresiva: "))

print(f"\n¡CUENTA PROGRESIVA DESDE 0 HASTA {N}!")
print("=" * 40)

contador = 0  # Variable que iniciará desde 0

while contador <= N:
    print(f"Número: {contador}")
    contador = contador + 1  # Incremento en 1

print("=" * 40)
print("¡CUENTA FINALIZADA! ✅")