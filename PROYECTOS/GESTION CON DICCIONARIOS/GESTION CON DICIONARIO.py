# 1. Inicializar un diccionario con 3 productos y sus precios
inventario = {
    "manzana": 0.50,
    "pan": 1.20,
    "leche": 0.95
}

print("Inventario inicial:", inventario)

# 2. Añadir un nuevo producto
inventario["huevos"] = 2.50
print("Después de añadir 'huevos':", inventario)

# 3. Actualizar el precio de un producto existente
inventario["pan"] = 1.35
print("Después de actualizar 'pan':", inventario)

# 4. Imprimir el diccionario final
print("\n--- Inventario final ---")
print(inventario)