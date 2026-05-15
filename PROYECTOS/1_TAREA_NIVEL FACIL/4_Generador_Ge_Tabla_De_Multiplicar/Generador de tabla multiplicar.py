# Solicitar un número al usuario
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"\n📊 TABLA DE MULTIPLICAR DEL {numero}")
print("=" * 35)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i:2} = {resultado:3}")

print("=" * 35)
print("¡Tabla completada! 2")