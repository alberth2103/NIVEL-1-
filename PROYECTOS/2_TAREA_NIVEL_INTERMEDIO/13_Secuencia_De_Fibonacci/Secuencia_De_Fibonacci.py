# Juego: Adivina el número secreto
NUMERO_SECRETO = 42  # Constante con el número a adivinar

print("=" * 50)
print("🎮 ¡BIENVENIDO AL JUEGO DE ADIVINANZAS! 🎮")
print("=" * 50)
print("He pensado un número secreto entre 1 y 100")
print("¿Podrás adivinarlo?")
print("-" * 50)

while True:  # Bucle infinito
    # Pedir al usuario que ingrese un número
    intento = int(input("\n🔢 Ingresa tu número: "))
    
    # Verificar si acertó
    if intento == NUMERO_SECRETO:
        print(f"\n🎉 ¡FELICITACIONES! 🎉")
        print(f"✅ ¡Adivinaste! El número secreto era {NUMERO_SECRETO}")
        print("🏆 ¡Eres un Brujo de las adivinanzas!")
        break  # Salir del bucle al acertar
    elif intento < NUMERO_SECRETO:
        print("📈 El número secreto es MAYOR. ¡Sigue intentando!")
    else:  # intento > NUMERO_SECRETO
        print("📉 El número secreto es MENOR. ¡Sigue intentando!")

print("=" * 50)
print("👋 ¡Gracias por jugar!")

# 1. Definir el número secreto
# NUMERO_SECRETO = 42
# Usamos mayúsculas porque es una constante (no cambia)
# El número 42 es famoso (La guía del autoestopista galáctico)
# 2. Mensaje de bienvenida
# print("=" * 50)
# print("🎮 ¡BIENVENIDO AL JUEGO DE ADIVINANZAS! 🎮")
# ecoración para hacer el juego más atractivo
# 3. Bucle infinito con while True
# while True:
# while True crea un bucle infinito
# Se ejecutará para siempre a menos que encuentre un break
# Perfecto para cuando no sabemos cuántas iteraciones serán necesarias
# 4. Solicitar un número al usuario
# intento = int(input("\n🔢 Ingresa tu número: "))
# input() pide al usuario que escriba
# int() convierte el texto a número entero
# El intento se almacena en la variable
# 5. Comparar con el número secreto
# if intento == NUMERO_SECRETO:
# ACIERTO
# elif intento < NUMERO_SECRETO:
# ES MENOR
# else:
# ES MAYOR
# 6. La magia de break
# break
# Cuando el usuario acierta, break sale del bucle inmediatamente
# Termina el while True y el programa continúa después del bucle
# 7. Pistas para ayudar
# elif intento < NUMERO_SECRETO:
# print("📈 El número secreto es MAYOR")
# else:
# print("📉 El número secreto es MENOR")
# #Si el intento es menor, decimos que es MAYOR
# Si el intento es mayor, decimos que es MENOR