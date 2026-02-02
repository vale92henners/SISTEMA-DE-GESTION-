def validar_entero(mensaje):
    """Valida que la entrada sea un número entero positivo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El número debe ser positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número válido.")