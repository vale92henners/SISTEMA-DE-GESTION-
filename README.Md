# Sistema de Gestión de Productos 

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

## Justificación Técnica 
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

Durante el desarrollo de este sistema de gestión, me enfrenté a retos que pusieron a prueba mis habilidades de lógica y estructuración de código. Aquí detallo los puntos más complejos y cómo logré superarlos:


La Transición a la Modularidad: Uno de mis mayores desafíos fue fragmentar la lógica que inicialmente tenía en un solo archivo hacia una arquitectura modular. Lo solucioné organizando el proyecto en una carpeta /modulos/ con archivos específicos para validaciones, gestión de datos y menús, lo que me permitió mantener un main.py limpio y fácil de leer.

Garantizar la Unicidad de los Datos: Me preocupaba que el sistema permitiera ingresar el mismo producto varias veces. Para resolverlo, decidí implementar un set (ids_unicos) que actúa como un filtro de seguridad; ahora, antes de agregar cualquier producto a mi lista principal, el sistema verifica en el conjunto si el ID ya existe, asegurando la integridad de la base de datos.


Gestión de Errores de Usuario: Fue un reto evitar que el programa se detuviera (se "cayera") si el usuario ingresaba letras en lugar de números. Diseñé funciones de validación utilizando bloques try-except, obligando al sistema a solicitar el dato nuevamente de forma amable hasta recibir un valor válido.


Implementación de Lógica Recursiva: Aplicar la recursividad para el cálculo de impuestos fue un desafío conceptual importante. Lo solucioné creando una función que procesa la lista de precios de manera descendente, calculando el IVA de cada elemento y sumándolo al resultado de la siguiente llamada, lo que optimizó el procesamiento sin necesidad de bucles tradicionales.

Conexión del Flujo de Control: Al principio, el menú no reconocía las opciones de eliminar o calcular impuestos. Lo solucioné reestructurando mi bloque if-elif-else en el archivo principal, asegurándome de que cada entrada de texto del usuario estuviera correctamente vinculada a la función modular correspondiente.

