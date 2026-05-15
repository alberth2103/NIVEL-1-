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