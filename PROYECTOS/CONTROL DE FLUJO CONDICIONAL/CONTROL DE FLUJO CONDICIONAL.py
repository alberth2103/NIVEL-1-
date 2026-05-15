# Definir una variable para grados Celsius
temperatura = 40

# Usar estructuras if-elif-else
if temperatura <= 0:
    print(f"El agua a {temperatura}°C está en estado SÓLIDO (hielo)")
elif temperatura >= 100:
    print(f"El agua a {temperatura}°C está en estado GASEOSO (vapor)")
else:
    print(f"El agua a {temperatura}°C está en estado LÍQUIDO")

# Pruebas con diferentes temperaturas
print("\n--- Pruebas adicionales ---")
temperaturas = [-5, 0, 25, 99, 100, 120]

for temp in temperaturas:
    if temp <= 0:
        estado = "SÓLIDO"
    elif temp <= 99:
        estado = "LÍQUIDO"
    else:
        estado = "GASEOSO"
    print(f"{temp:3}°C → Estado {estado}")