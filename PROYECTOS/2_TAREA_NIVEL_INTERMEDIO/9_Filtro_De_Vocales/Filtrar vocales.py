# Pedir una frase al usuario
frase = input("Ingrese una frase: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Iterar sobre cada carácter de la frase
for letra in frase:
    if letra in "aeiouAEIOU":
        contador_vocales = contador_vocales + 1

# Mostrar el resultado
print(f"\n✅ La frase tiene {contador_vocales} vocal(es)")