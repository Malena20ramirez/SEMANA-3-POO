# Comparación entre Programación Tradicional y Programación Orientada a Objetos

## Autor


Ramirez Pacho Malena Jimena

 ## Descripción


Este repositorio Consiste en el desarrollo de un sistema básico para la gestión y registro de mascotas ( Nombre, Especie y Edad) bajo dos paradigmas de desarrollo de software:
1. Programación Tradicional (programacion_tradicional): Solución estructurada basada estrictamente en variables globales/locales y funciones secuenciales, prescindiendo del uso de abstracciones complejas o clases.
2. Programación Orientada a Objetos (programacion_poo): Solución modularizada donde la entidad del mundo real se abstrae dentro de una clase (Mascota) que encapsula sus atributos y comportamientos (mostrar_informacion y hacer_sonido), distribuyendo la lógica de manera limpia entre módulos.

## Estructura del proyecto

```text
programacion_tradicional/
└── tradicional.py

programacion_poo/
├── libro.py
└── main.py
```
## Reflexión
Al implementar el mismo requerimiento bajo ambos enfoques se identificaron diferencias fundamentales en el diseño y la escalabilidad del software:

* **Organización y Estructura del Código:** En la programación tradicional, la información viaja de forma suelta mediante estructuras de datos simples como diccionarios. En cambio, la POO nos permite empaquetar de forma elegante tanto los datos (atributos) como las acciones que estos pueden realizar (métodos) en un solo bloque o molde reutilizable.
* **Mantenimiento y Escalabilidad:** Si el sistema de gestión de mascotas requiriera añadir nuevas propiedades en el futuro (como registros médicos o alimentación), el enfoque tradicional obligaría a modificar múltiples funciones de lectura y formateo, incrementando el riesgo de errores. Con la POO, basta con extender la clase Mascota o usar principios como la herencia, manteniendo el código del archivo principal (main.py) intacto y limpio.
* **Modularidad y Abstracción:** La separación en archivos (mascota.py y main.py) que ofrece la POO facilita la legibilidad y el trabajo colaborativo, permitiendo que la lógica del negocio esté completamente aislada de la interfaz de interacción con el usuario.