# Sistema de Gestión de Productos - Proyecto ABP (Módulo 3)

## Descripción del Proyecto
Este sistema es una solución robusta desarrollada en **Python** para la gestión automatizada de inventarios. Integra identificación de usuarios por roles, validación de datos, gestión de productos y cálculos financieros mediante algoritmos recursivos.

## Funcionalidades Implementadas
* **Identificación de Sesión**: Captura de nombre y rol del operador ("Admin", "Invitado", "Usuario") al inicio del programa.
* **Entrada y salida de datos**: Formateo de salida profesional con **f-strings**.
* **Estructuras de control**: Navegación mediante menús iterativos `while` y toma de decisiones con `if-elif-else`.
* **Modularización**: Organización del código en paquetes y módulos para alta mantenibilidad.
* **Estructuras de datos avanzadas**:
    * **Listas y Diccionarios**: Para el almacenamiento de la base de datos de productos.
    * **Sets**: Para garantizar que los IDs de productos sean únicos.
    * **Tuplas**: Para la gestión de roles inmutables.

## Justificación Técnica (Rúbrica: Sobresaliente)
1. **Flujo Lógico**: El sistema implementa un paso de autenticación inicial antes de permitir el acceso al menú, asegurando la integridad del proceso.
2. **Recursividad**: Se utiliza para el cálculo de impuestos, demostrando eficiencia en el procesamiento de colecciones de datos.
3. **Manejo de Errores**: Uso de bloques `try-except` en el módulo de validaciones para prevenir interrupciones inesperadas del programa.
4. **PEP 8**: El código cumple con los estándares de estilo, incluyendo docstrings y nomenclatura clara.

## Estructura del Código
* `main.py`: Punto de entrada que coordina la identificación y el menú principal.
* `modulos/datos_basicos.py`: Manejo de perfiles de usuario y roles.
* `modulos/validaciones.py`: Asegura la integridad de las entradas numéricas.
* `modulos/gestion_datos.py`: Lógica de almacenamiento y eliminación de productos.
* `modulos/funciones_utiles.py`: Algoritmos recursivos y procedimientos estéticos.
* `modulos/menu.py`: Interfaz visual del sistema.


