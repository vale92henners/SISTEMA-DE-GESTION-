def capturar_usuario():
    """
    Captura información básica del usuario utilizando input() y f-strings[cite: 757, 818].
    """
    nombre = input("Ingrese su nombre de operador: ")
    # Uso de tuplas para datos inmutables (Roles de usuario)[cite: 772, 852].
    ROLES = ("Admin", "Invitado", "Usuario")
    
    print(f"Roles disponibles: {ROLES}")
    rol = input("Asigne su rol para esta sesión: ")
    
    return {"operador": nombre, "rol": rol} # Retorna un diccionario [cite: 771]