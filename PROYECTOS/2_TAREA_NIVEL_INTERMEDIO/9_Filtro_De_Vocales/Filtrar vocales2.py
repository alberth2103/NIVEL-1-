frase = input("Ingrese una frase: ")
frase = frase.lower()

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in frase:
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contador_u += 1

total = contador_a + contador_e + contador_i + contador_o + contador_u

print(f"\n📊 DESGLOSE DE VOCALES:")
print(f"   • Vocal 'a': {contador_a}")
print(f"   • Vocal 'e': {contador_e}")
print(f"   • Vocal 'i': {contador_i}")
print(f"   • Vocal 'o': {contador_o}")
print(f"   • Vocal 'u': {contador_u}")
print(f"   • TOTAL: {total} vocales")

