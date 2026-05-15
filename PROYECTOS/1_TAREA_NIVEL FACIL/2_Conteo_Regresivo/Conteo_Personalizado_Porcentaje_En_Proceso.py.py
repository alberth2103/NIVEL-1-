N = int(input("Ingrese el número límite: "))
contador = 0

print(f"Progreso: 0% hasta {N}")
print("=" * 40)

while contador <= N:
    porcentaje = (contador / N) * 100 if N > 0 else 100
    print(f"Número: {contador} | Progreso: {porcentaje:.0f}%")
    contador += 1

print("=" * 40)
print("¡100% COMPLETADO! ✅")