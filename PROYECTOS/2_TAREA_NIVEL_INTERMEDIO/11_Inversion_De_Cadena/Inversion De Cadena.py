# Invertir una palabra usando for
palabra = input("Ingrese una palabra: ")

palabra_invertida = ""  # Cadena vacía para construir la palabra invertida

for letra in palabra:
    palabra_invertida = letra + palabra_invertida  # Concatenar al inicio

print(f"\n✅ Palabra original: {palabra}")
print(f"✅ Palabra invertida: {palabra_invertida}")

# Usando bucle while
# Invertir una palabra usando while
# palabra = input("Ingrese una palabra: ")
# palabra_invertida = ""  # Cadena vacía
# indice = len(palabra) - 1  # Empezamos desde el último carácter
# while indice >= 0:
# palabra_invertida = palabra_invertida + palabra[indice]  # Concatenar al final
# indice = indice - 1  # Decrementar índice
# print(f"\n✅ Palabra original: {palabra}")
# print(f"✅ Palabra invertida: {palabra_invertida}")