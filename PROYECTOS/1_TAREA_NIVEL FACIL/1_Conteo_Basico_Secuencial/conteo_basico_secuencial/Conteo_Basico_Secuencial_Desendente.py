# Imprimir en una sola línea
for numero in range(15, 0, -1):
    print(numero, end=" ")
# Salida: 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1


#La función range()
#range(1, 16)

#range(inicio, fin) genera una secuencia de números
#inicio = 1 → comienza en el número 1
#fin = 16 → termina ANTES del 16 (es decir, en el 15)

#Regla importante: range() incluye el inicio pero NO incluye el fin

#El bucle for
#for numero in range(1, 16):
#Importante: El fin debe ser MENOR que el inicio cuando usas paso negativo, de lo contrario no se generarán números.