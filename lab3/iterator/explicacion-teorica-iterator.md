**Patrón de diseño iterador**

Consiste en un objeto que permite recorrer una colección como si fuera una lista, independientemente de su estructura, y posicionarse sobre cualquiera de sus elementos. Es un patrón de comportamiento. Este patrón al permitir posicionarse sobre elementos específicos de la colección para la cual se implemente, permite evitar muchas lecturas innecesarias en cierto tipo de estructuras como los árboles, en los cuales para obtener cada elemnto tiene que recorrerse una y otra vez desde la raíz.


Iterator contribuye al mantenimiento y escalabilidad abstrayendo la forma en que se recorre una colección, disminuyendo la cantidad de cambios necesarios si la colección cambia, y despreocupando a los clientes de la clase de cuál sea la estructura lógica de la colección.


**Otras ventajas y desventajas**


Ventajas


-Puede contener toda la responsabilidad sobre los distintos tipos de recorridos que se necesiten hacer sobre una colección.
-Puede reutilizarse para distintas colecciones.
-Los clientes de la clase no tiene que pensar en estructuras lógicas de colecciones.


Desventajas

-Dificil de implementar para ciertas estructuras de datos.
-Es un paso más para el acceso a una colección, lo cual puede disminuir la eficiencia en bucles.


**Ejemplos de casos de uso**

-Para paginación: Se pueden abstraer las colecciones en subcolecciones que representan páginas, las cuales son subcolecciones de elementos. Eso permite administrar mejor la memoria al visualizar u operar sobre grandes colecciones de datos.


-Para facilitar el uso de colecciones: Por ejemplo se pueden acceder a los elementos de un arbol como si fuera una lista.


-Para cumplir Single Responsability de SOLID: Esto porque la clase Iterator puede contener toda la funcionalidad que la clase de la colección no contiene, en vez de implementar dicha funcionalidad en clases que se hicieron con otros propósitos.