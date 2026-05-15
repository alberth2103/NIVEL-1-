# ==========================================
# CAJERO AUTOMÁUTICO
# ==========================================
# PIN válido: 1234
# Saldo inicial: $5000

# Variables iniciales
PIN_CORRECTO = "1234"
saldo = 5000
intentos = 0

print("=" * 65)
print("     BIENVENIDO AL CAJERO AUTOMÁTICO BANCO FEDERAL")
print("=" * 65)

# ========== VALIDACIÓN DEL PIN (bucle while) ==========
while intentos < 3:
    pin_ingresado = input("\nIngrese su PIN (4 dígitos): ")
    
    if pin_ingresado == PIN_CORRECTO:
        print("\n✅ PIN CORRECTO. Acceso concedido.\n")
        break  # PIN correcto, salimos del bucle de intentos
    else:
        intentos += 1
        intentos_restantes = 3 - intentos
        if intentos_restantes > 0:
            print(f"❌ PIN incorrecto. Le quedan {intentos_restantes} intento(s).")
        else:
            print("🔒 CUENTA BLOQUEADA. Demasiados intentos fallidos.")
            exit()  # Termina el programa por bloqueo

# ========== MENÚ PRINCIPAL (bucle while) ==========
while True:
    # Mostrar menú
    print("\n" + "-" * 40)
    print("CAJERO AUTOMÁTICO - MENÚ PRINCIPAL")
    print("-" * 40)
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    print("-" * 40)
    
    opcion = input("Seleccione una opción (1-4): ")
 # ========== OPCIÓN 1: CONSULTAR SALDO ==========
    if opcion == "1":
        print(f"\n💰 Su saldo actual es: ${saldo:.2f}")
        input("\nPresione ENTER para continuar...")  # 👈 PAUSA hasta que el usuario presione una tecla
    
    # ========== OPCIÓN 2: DEPOSITAR ==========
    elif opcion == "2":
        print("\n--- DEPÓSITO ---")
        try:
            deposito = float(input("Monto a depositar: $"))
            if deposito > 0:
                saldo = saldo + deposito  # Operador aritmético (+)
                print(f"✅ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("❌ El monto debe ser mayor que cero.")
        except ValueError:
            print("❌ Ingrese un monto válido.")
    
    # ========== OPCIÓN 3: RETIRAR ==========
    elif opcion == "3":
        print("\n--- RETIRO ---")
        try:
            monto = float(input("Monto a retirar: $"))
            
            # Validación con operadores lógicos (and, or)
            # Verifica: monto positivo AND saldo suficiente AND múltiplo de 10
            if monto > 0 and monto <= saldo and monto % 10 == 0:
                
                # Actualizar saldo con operador aritmético (-)
                saldo = saldo - monto
                monto = int(monto)  # Convertir a entero para billetes
                
                print(f"\n✅ Retiro exitoso: ${monto}")
                print(f"💰 Nuevo saldo: ${saldo:.2f}")
                
                # ========== CÁLCULO DE BILLETES ==========
                # División entera (//) para cantidad de billetes
                # Módulo (%) para obtener el resto
                
                billetes_100 = monto // 100
                resto = monto % 100
                
                billetes_50 = resto // 50
                resto = resto % 50
                
                billetes_20 = resto // 20
                resto = resto % 20
                
                billetes_10 = resto // 10
                resto = resto % 10
                
                # Mostrar desglose de billetes
                print("\n--- DESGLOSE DE BILLETES ---")
                if billetes_100 > 0:
                    print(f"  ${100}: {billetes_100} billete(s)")
                if billetes_50 > 0:
                    print(f"  ${50}: {billetes_50} billete(s)")
                if billetes_20 > 0:
                    print(f"  ${20}: {billetes_20} billete(s)")
                if billetes_10 > 0:
                    print(f"  ${10}: {billetes_10} billete(s)")
                print("-" * 30)
                
            else:
                # Validación con operadores lógicos para mensajes específicos
                if monto <= 0:
                    print("❌ El monto debe ser mayor que cero.")
                elif monto > saldo:
                    print(f"❌ Saldo insuficiente. Su saldo actual es: ${saldo:.2f}")
                elif monto % 10 != 0:
                    print("❌ El monto debe ser múltiplo de 10.")
                else:
                    print("❌ Monto inválido.")
                    
        except ValueError:
            print("❌ Ingrese un monto numérico válido.")
    
    # ========== OPCIÓN 4: SALIR ==========
    elif opcion == "4":
        print("\n✨ Gracias por usar nuestro cajero.")
        print("   ¡Hasta luego!")
        break  # Sale del bucle while del menú principal
    
    # ========== OPCIÓN INVÁLIDA ==========
    else:
        print("❌ Opción no válida. Seleccione 1, 2, 3 o 4.")

print("\n" + "=" * 50)
print("       PROGRAMA FINALIZADO")
print("=" * 50)















#📌 LÍNEAS 1-8: CABECERA Y VARIABLES INICIALES

# ==========================================
# CAJERO AUTOMÁUTICO
# ==========================================
# Líneas 1-4: Comentarios decorativos que indican el título del programa. No afectan la ejecución.

# # PIN válido: 1234
# Saldo inicial: $5000
# Líneas 6-7: Comentarios informativos que documentan el PIN correcto y el saldo inicial.
# Variables iniciales
# PIN_CORRECTO = "1234"
# saldo = 5000
# intentos = 0
# Línea 9: Comentario que indica que siguen variables.
# Línea 10: PIN_CORRECTO = "1234" - Variable que almacena el PIN válido como texto (string).
# Línea 11: saldo = 5000 - Variable numérica que guarda el saldo actual de la cuenta.
# Línea 12: intentos = 0 - Contador que lleva cuántas veces el usuario ha ingresado mal el PIN.
# 📌 LÍNEAS 14-17: MENSAJE DE BIENVENIDA
# print("=" * 65)
# print("     BIENVENIDO AL CAJERO AUTOMÁTICO BANCO FEDERAL")
# print("=" * 65)
# Línea 14: print("=" * 65) - Imprime 65 símbolos =, creando una línea decorativa.
# Línea 15: Imprime el mensaje de bienvenida centrado.
# Línea 16: Otra línea decorativa con 65 símbolos =.
# 📌 LÍNEAS 19-33: VALIDACIÓN DEL PIN (BUCLE WHILE)
# ========== VALIDACIÓN DEL PIN (bucle while) ==========
# while intentos < 3:
# Línea 19: Comentario indicativo.
# Línea 20: while intentos < 3: - Inicia un bucle que se repite mientras el número de intentos fallidos sea menor a 3.
# pin_ingresado = input("\nIngrese su PIN (4 dígitos): ")
# Línea 21: input() - Solicita al usuario que ingrese su PIN. El \n agrega una línea en blanco antes. El valor se guarda en pin_ingresado como texto.
# if pin_ingresado == PIN_CORRECTO:
# print("\n✅ PIN CORRECTO. Acceso concedido.\n")
# break  # PIN correcto, salimos del bucle de intentos
# Línea 23: if pin_ingresado == PIN_CORRECTO: - Compara lo ingresado con el PIN correcto.
# Línea 24: Si son iguales, imprime mensaje de éxito con emoji ✅.
# Línea 25: break - Sale del bucle while (termina la validación del PIN).
# else:
# intentos += 1
# intentos_restantes = 3 - intentos
# Línea 27: else: - Se ejecuta si el PIN es incorrecto.
# Línea 28: intentos += 1 - Incrementa el contador de fallos en 1 (equivale a intentos = intentos + 1).
# Línea 29: intentos_restantes = 3 - intentos - Calcula cuántos intentos le quedan al usuario.
# if intentos_restantes > 0:
# print(f"❌ PIN incorrecto. Le quedan {intentos_restantes} intento(s).")
# else:
# print("🔒 CUENTA BLOQUEADA. Demasiados intentos fallidos.")
# exit()  # Termina el programa por bloqueo
# Línea 31: if intentos_restantes > 0: - Si todavía quedan intentos...
# Línea 32: Muestra mensaje de error con emoji ❌ y los intentos restantes.
# Línea 33: else: - Si no quedan intentos (agotó los 3)...
# Línea 34: Muestra mensaje de bloqueo con emoji 🔒.
# Línea 35: exit() - Termina completamente el programa.
# 📌 LÍNEAS 38-52: MENÚ PRINCIPAL (ENCABEZADO)
# ========== MENÚ PRINCIPAL (bucle while) ==========
# while True:
# Línea 38: Comentario indicativo.
# Línea 39: while True: - Bucle infinito que mantiene el menú repitiéndose hasta que el usuario elija "Salir".
# Mostrar menú
# print("\n" + "-" * 40)
# print("CAJERO AUTOMÁTICO - MENÚ PRINCIPAL")
# print("-" * 40)
# print("2. Depositar dinero")
# print("3. Retirar dinero")
# print("4. Salir")
# print("-" * 40)
# Línea 41: Comentario.
# Línea 42: print("\n" + "-" * 40) - Imprime línea en blanco + 40 guiones.
# Línea 43: Título del menú.
# Línea 44: 40 guiones.
# Líneas 45-48: Las 4 opciones del menú.
# Línea 49: 40 guiones.
# opcion = input("Seleccione una opción (1-4): ")
# Línea 51: Solicita al usuario que elija una opción y la guarda en opcion como texto.
# 📌 LÍNEAS 52-58: OPCIÓN 1 - CONSULTAR SALDO
# ========== OPCIÓN 1: CONSULTAR SALDO ==========
# if opcion == "1":
# print(f"\n💰 Su saldo actual es: ${saldo:.2f}")
# input("\nPresione ENTER para continuar...")
# Línea 53: Comentario (nota: tiene un espacio al inicio que no afecta).
# Línea 54: if opcion == "1": - Si el usuario eligió la opción 1...
# Línea 55: print(f"\n💰 Su saldo actual es: ${saldo:.2f}") - Muestra el saldo actual. El :.2f formatea el número con 2 decimales.
# Línea 56: input("\nPresione ENTER para continuar...") - Pausa el programa hasta que el usuario presione ENTER, permitiéndole leer el saldo.
# 📌 LÍNEAS 59-69: OPCIÓN 2 - DEPOSITAR
# ========== OPCIÓN 2: DEPOSITAR ==========
# elif opcion == "2":
# print("\n--- DEPÓSITO ---")
# try:
# deposito = float(input("Monto a depositar: $"))
# Línea 59: Comentario.
# Línea 60: elif opcion == "2": - Si la opción es 2 (solo si no fue 1).
# Línea 61: Imprime "--- DEPÓSITO ---".
# Línea 62: try: - Inicia un bloque para capturar errores (si el usuario ingresa texto en lugar de números).
# Línea 63: deposito = float(input("Monto a depositar: $")) - Solicita el monto y lo convierte a número decimal.
# if deposito > 0:
# saldo = saldo + deposito
# print(f"✅ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
# else:
# print("❌ El monto debe ser mayor que cero.")
# Línea 65: if deposito > 0: - Verifica que el depósito sea positivo.
# Línea 66: saldo = saldo + deposito - Operador aritmético (+) para sumar al saldo.
# Línea 67: Muestra mensaje de éxito con el nuevo saldo.
# Línea 68: else: - Si el monto no es positivo...
# Línea 69: Muestra mensaje de error.
# except ValueError:
# print("❌ Ingrese un monto válido.")
# Línea 71: except ValueError: - Si ocurre un error al convertir a número (ingresó letras)...
# Línea 72: Muestra mensaje de error.
# 📌 LÍNEAS 74-122: OPCIÓN 3 - RETIRAR (LA MÁS COMPLEJA)
# ========== OPCIÓN 3: RETIRAR ==========
# elif opcion == "3":
# print("\n--- RETIRO ---")
# try:
# monto = float(input("Monto a retirar: $"))
# Línea 74: Comentario.
# Línea 75: elif opcion == "3": - Si eligió la opción 3.
# Línea 76: Imprime "--- RETIRO ---".
# Línea 77: try: - Bloque para capturar errores.
# Línea 78: Solicita el monto a retirar y lo convierte a número decimal.
# Validación con operadores lógicos (and, or)
# if monto > 0 and monto <= saldo and monto % 10 == 0:
# Línea 80: Comentario.
# Línea 81: if monto > 0 and monto <= saldo and monto % 10 == 0: - Operadores lógicos (AND) que verifican TRES condiciones simultáneamente:
# monto > 0 → el monto es positivo
# monto <= saldo → hay suficiente saldo
# monto % 10 == 0 → el monto es múltiplo de 10
# Actualizar saldo con operador aritmético (-)
# saldo = saldo - monto
# monto = int(monto)
# Línea 83: Comentario.
# Línea 84: saldo = saldo - monto - Operador aritmético (-) para restar del saldo.
# Línea 85: monto = int(monto) - Convierte el monto a entero (sin decimales) para calcular billetes.
# print(f"\n✅ Retiro exitoso: ${monto}")
# print(f"💰 Nuevo saldo: ${saldo:.2f}")
# Línea 87: Muestra mensaje de éxito con el monto retirado.
# Línea 88: Muestra el nuevo saldo actualizado.
# ========== CÁLCULO DE BILLETES ==========
# billetes_100 = monto // 100
# resto = monto % 100
# Línea 90: Comentario.
# Línea 91: billetes_100 = monto // 100 - División entera (//) : Cuántas veces cabe 100 en el monto. Ej: 380 // 100 = 3.
# Línea 92: resto = monto % 100 - Módulo (%) : Lo que sobra después de quitar los billetes de 100. Ej: 380 % 100 = 80.
# es_50 = resto // 50
# resto = resto % 50
# Línea 94: billetes_50 = resto // 50 - Cuántos billetes de 50 caben en el resto (80 // 50 = 1).
# Línea 95: resto = resto % 50 - Nuevo resto (80 % 50 = 30).
# billetes_20 = resto // 20
# resto = resto % 20
# Línea 97: billetes_20 = resto // 20 - Billetes de 20 (30 // 20 = 1).
# Línea 98: resto = resto % 20 - Resto actualizado (30 % 20 = 10).
# billetes_10 = resto // 10
# resto = resto % 10
# Línea 100: billetes_10 = resto // 10 - Billetes de 10 (10 // 10 = 1).
# Línea 101: resto = resto % 10 - Resto final (10 % 10 = 0).
# Mostrar desglose de billetes
# print("\n--- DESGLOSE DE BILLETES ---")
# if billetes_100 > 0:
# print(f"  ${100}: {billetes_100} billete(s)")
# if billetes_50 > 0:
# print(f"  ${50}: {billetes_50} billete(s)")
# if billetes_20 > 0:
# print(f"  ${20}: {billetes_20} billete(s)")
# if billetes_10 > 0:
# print(f"  ${10}: {billetes_10} billete(s)")
#                print("-" * 30)
# Línea 103: Comentario.

# Línea 104: Imprime título del desglose.

# Líneas 105-112: if condicionales que muestran solo los billetes que tienen cantidad > 0.

# Línea 113: Línea decorativa de 30 guiones.
#             else:
#                 # Validación con operadores lógicos para mensajes específicos
#                 if monto <= 0:
#                     print("❌ El monto debe ser mayor que cero.")
#                 elif monto > saldo:
#                     print(f"❌ Saldo insuficiente. Su saldo actual es: ${saldo:.2f}")
#                elif monto % 10 != 0:
#                    print("❌ El monto debe ser múltiplo de 10.")
#                else:
#                    print("❌ Monto inválido.")
# Línea 115: else: - Si NO se cumplió la condición principal (alguna validación falló).

# Línea 117: if monto <= 0: - Si el monto es negativo o cero...

# Línea 118: Mensaje correspondiente.

# Línea 119: elif monto > saldo: - Si el monto excede el saldo...

# Línea 120: Mensaje de saldo insuficiente.

# Línea 121: elif monto % 10 != 0: - Si no es múltiplo de 10...

# Línea 122: Mensaje de error.

# Línea 123: else: - Por si acaso...

# Línea 124: Mensaje genérico.


#        except ValueError:
#            print("❌ Ingrese un monto numérico válido.")
# Línea 127: Captura error si el usuario ingresó texto en lugar de números.

# Línea 128: Mensaje de error.

# 📌 LÍNEAS 130-136: OPCIÓN 4 - SALIR

    # ========== OPCIÓN 4: SALIR ==========
#    elif opcion == "4":
#        print("\n✨ Gracias por usar nuestro cajero.")
#        print("   ¡Hasta luego!")
#        break
# Línea 131: Comentario.

# Línea 132: elif opcion == "4": - Si eligió salir...

# Línea 133: Mensaje de agradecimiento con emoji ✨.

# Línea 134: Mensaje de despedida.

# Línea 135: break - Sale del bucle while True, terminando el programa.

# 📌 LÍNEAS 138-143: OPCIÓN INVÁLIDA Y FINAL

    # ========== OPCIÓN INVÁLIDA ==========
#    else:
#        print("❌ Opción no válida. Seleccione 1, 2, 3 o 4.")
# Línea 138: Comentario.

# Línea 139: else: - Si la opción NO es 1, 2, 3 ni 4...

# Línea 140: Mensaje de error por opción inválida.


# print("\n" + "=" * 50)
# print("       PROGRAMA FINALIZADO")
# print("=" * 50)
# Línea 143: Línea en blanco + 50 símbolos =.

# Línea 144: Mensaje de finalización.

#Línea 145: 50 símbolos =.

#🎯 RESUMEN DE CONCEPTOS CLAVE
# Concepto	Dónde aparece	Ejemplo
# Bucle while	PIN y menú	while intentos < 3:
# if-elif-else	Opciones del menú	if opcion == "1":
# Operadores lógicos	Validación retiro	and en monto > 0 and monto <= saldo
# Operador +	Depósito	saldo = saldo + deposito
# Operador -	Retiro	saldo = saldo - monto
# División entera //	Billetes de 100	billetes_100 = monto // 100
# Módulo %	Calcular restos	resto = monto % 100
# break	Salir de bucles	break en PIN correcto y opción salir
# try-except	Manejo de errores	Capturar entradas no numéricas
