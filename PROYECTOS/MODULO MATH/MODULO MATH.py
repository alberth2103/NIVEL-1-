import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo usando math.pi y math.pow
    
    Args:
        radio (float): Radio del círculo
        
    Returns:
        float: Área del círculo
    """
    area = math.pi * math.pow(radio, 2)
    return area

# Ejemplo de uso
if __name__ == "__main__":
    # Prueba con diferentes radios
    radio_ejemplo = 10
    resultado = calcular_area_circulo(radio_ejemplo)
    print(f"El área del círculo con radio {radio_ejemplo} es: {resultado:.2f}")