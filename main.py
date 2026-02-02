import modulos.menu as menu
import modulos.gestion_datos as gestion
import modulos.funciones_utiles as funciones
import modulos.datos_basicos as datos_basicos # Importamos el módulo de usuario
from modulos.validaciones import validar_entero

def ejecutar_sistema():
    #  Identificación del usuario 
    usuario_info = datos_basicos.capturar_usuario()
    funciones.mostrar_encabezado_descriptivo(usuario_info['operador'])
    print(f"Sesión iniciada como: {usuario_info['rol']}")

    # Inicio del menú principal
    while True:
        menu.mostrar_opciones()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = validar_entero("Ingrese ID del producto: ")
            nom = input("Nombre del producto: ")
            pre = validar_entero("Precio: ")
            exito, msj = gestion.agregar_producto(id_p, nom, pre)
            print(msj)

        elif opcion == "2":
            gestion.listar_productos()
        
        elif opcion == "3":
            id_a_eliminar = validar_entero("Ingrese el ID del producto a eliminar: ")
            gestion.eliminar_producto(id_a_eliminar)

        elif opcion == "4":
            precios = [p['precio'] for p in gestion.productos]
            if precios:
                total_impuesto = funciones.calcular_impuesto_recursivo(precios)
                print(f"El impuesto total acumulado (19% IVA) es: ${total_impuesto}")
            else:
                print("No hay productos para calcular impuestos.")

        elif opcion == "0":
            print(f"Cerrando sesión de {usuario_info['operador']}...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_sistema()