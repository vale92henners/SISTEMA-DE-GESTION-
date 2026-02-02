# Lista para almacenar productos como diccionarios [cite: 851]
productos = []
# Set para asegurar que los IDs sean únicos [cite: 853]
ids_unicos = set()

def agregar_producto(id_prod, nombre, precio):
    if id_prod in ids_unicos:
        return False, "El ID ya existe."
    
    # Creamos el producto como diccionario [cite: 851]
    nuevo_producto = {
        "id": id_prod,
        "nombre": nombre,
        "precio": precio
    }
    productos.append(nuevo_producto) # [cite: 854]
    ids_unicos.add(id_prod)
    return True, "Producto agregado con éxito."

def listar_productos():
    if not productos:
        print("No hay productos registrados.")
    for p in productos:
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Precio: ${p['precio']}")

def eliminar_producto(id_prod):
    """Busca y elimina un producto por su ID."""
    global productos, ids_unicos
    for p in productos:
        if p['id'] == id_prod:
            productos.remove(p) # Uso de métodos de lista [cite: 770, 854]
            ids_unicos.remove(id_prod) # Uso de métodos de set [cite: 773, 853]
            print(f"Producto {id_prod} eliminado.")
            return
    print("No se encontró el producto.")