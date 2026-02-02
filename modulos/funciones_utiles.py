def calcular_impuesto_recursivo(lista_precios, tasa=0.19):
    """
    Calcula el impuesto total de una lista de precios de forma recursiva[cite: 768].
    
    Argumentos:
        lista_precios (list): Lista con los precios de los productos.
        tasa (float): Porcentaje de impuesto (default 19% IVA).
    Retorno:
        float: El total de impuestos acumulados[cite: 767].
    """
    if not lista_precios:
        return 0
    else:
        # Suma el impuesto del primer elemento y llama a la función con el resto [cite: 645]
        return (lista_precios[0] * tasa) + calcular_impuesto_recursivo(lista_precios[1:], tasa)

def mostrar_encabezado_descriptivo(nombre_usuario):
    """
    Procedimiento para mostrar un saludo personalizado al iniciar[cite: 807, 863].
    """
    print(f"Bienvenido al sistema, {nombre_usuario}. Preparando entorno...")