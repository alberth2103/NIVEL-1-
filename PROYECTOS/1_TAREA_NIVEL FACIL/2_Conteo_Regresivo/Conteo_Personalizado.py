N = int(input("Ingrese el número límite: "))
contador = 0

print(f"\nContando desde 0 hasta {N}")
print("-" * 30)

while contador <= N:
    if contador == N:
        print(f"¡Llegamos a {contador}! 🎯")
    else:
        print(f"Progreso: {contador}")
    contador += 1

print("¡Proceso completado!")