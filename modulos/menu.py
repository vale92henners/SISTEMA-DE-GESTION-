def mostrar_opciones():
    """
    Procedimiento que imprime el menú principal en pantalla.
    Utiliza f-strings para un formato limpio[cite: 758, 863].
    """
    print("\n" + "="*30)
    print(f"{'SISTEMA DE GESTIÓN':^30}")
    print("="*30)
    print("1. Registrar nuevo producto")
    print("2. Listar todos los productos")
    print("3. Eliminar un producto")
    print("4. Calcular impuesto total ")
    print("0. Salir")
    print("="*30)