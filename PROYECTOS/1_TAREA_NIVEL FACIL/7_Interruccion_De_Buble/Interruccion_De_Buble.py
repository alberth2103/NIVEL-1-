# Iterar del 1 al 100 y encontrar el primer número divisible por 13
print("Buscando el primer número divisible por 13 entre 1 y 100...")
print("=" * 50)

for numero in range(1, 101):
    if numero % 13 == 0:
        print(f"✅ ¡ENCONTRADO! El número {numero} es divisible por 13")
        print(f"   → {numero} ÷ 13 = {numero // 13}")
        break  # Detiene todo el bucle
    else:
        print(f"❌ {numero} no es divisible por 13")

print("=" * 50)
print("Bucle terminado por 'break'")


# 1- El bucle for
# for numero in range(1, 101):
# range(1, 101) genera números del 1 al 100
# La variable numero toma cada valor: 1, 2, 3, ..., 100
# Normalmente recorrería los 100 números, pero break lo detendrá antes
# La condición if (divisibilidad)

# 2-if numero % 13 == 0:
# % es el operador módulo (residuo de la división)
# numero % 13 calcula el residuo al dividir por 13
# Si el residuo es 0, significa que es divisible por 13
# Ejemplo: 26 % 13 = 0 → 26 es divisible por 13

# 3-La magia de break
# break
# break es una palabra mágica que detiene inmediatamente el bucle
# Sale del bucle sin importar cuántas iteraciones faltaban
# El programa continúa con el código que está después del bucle
# 4. El bloque else (opcional para depuración)
# else:
# print(f"❌ {numero} no es divisible por 13")
