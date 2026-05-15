# Validar que el usuario ingrese un número positivo
numero = int(input("Ingrese un número positivo: "))

# Mientras el número NO sea positivo, seguir preguntando
while numero <= 0:
    print("❌ Error: El número debe ser POSITIVO (mayor que 0)")
    numero = int(input("Ingrese un número positivo: "))

print(f"\n✅ ¡Correcto! Ingresaste el número positivo: {numero}")


# Primera solicitud (fuera del bucle)
# numero = int(input("Ingrese un número positivo: "))
# Pedimos el número una vez antes de entrar al bucle
# Esto permite que el usuario tenga una oportunidad inicial
# 2. La condición del while
# while numero <= 0:
# Condición de ERROR: Mientras el número sea menor o igual a 0
# Mientras sea True (número inválido), el bucle se ejecuta
# Cuando sea False (número válido), el bucle termina
# 3. Mensaje de error y repetición
# print("❌ Error: El número debe ser POSITIVO (mayor que 0)")
# numero = int(input("Ingrese un número positivo: "))
# Mostramos por qué es inválido
# Volvemos a pedir el número
# Actualizamos la variable numero
# 4. Confirmación final
# print(f"\n✅ ¡Correcto! Ingresaste el número positivo: {numero}")