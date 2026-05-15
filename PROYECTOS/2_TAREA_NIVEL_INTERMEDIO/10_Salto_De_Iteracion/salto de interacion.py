# Imprimir números del 1 al 20 saltando los múltiplos de 3
print("NÚMEROS DEL 1 AL 20 (EXCLUYENDO MÚLTIPLOS DE 3)")
print("=" * 45)

for numero in range(1, 21):
    if numero % 3 == 0:
        continue  # Salta a la siguiente iteración
    print(numero)

print("=" * 45)
print("✅ Programa completado")

# 1. El bucle for
# for numero in range(1, 21):
# range(1, 21) genera números del 1 al 20
# La variable numero toma cada valor: 1, 2, 3, ..., 20
#2. La condición if (múltiplos de 3)
# if numero % 3 == 0:
# % es el operador módulo (residuo de la división)
# numero % 3 calcula el residuo al dividir por 3
# Si el residuo es 0, significa que es múltiplo de 3
# Ejemplos: 3 % 3 = 0, 6 % 3 = 0, 9 % 3 = 0, etc.
# 3. La magia de continue
#continue es una palabra clave que salta el resto del código en la iteración actual
# No sale del bucle (a diferencia de break)
# Simplemente pasa a la siguiente iteración inmediatamente
# 4. Imprimir el número
# print(numero)
# Solo se ejecuta si el número NO es múltiplo de 3
# Si continue se activó, esta línea se salta