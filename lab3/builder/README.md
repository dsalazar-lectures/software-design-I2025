# OrderBuilder Demo

## Descripción
Este proyecto muestra cómo usar el **patrón Builder** para crear objetos `Order` de forma fluida y garantizar su inmutabilidad y validación centralizada. Es perfecto para aplicaciones de e-commerce, ERP o cualquier dominio que maneje pedidos con muchos atributos opcionales.

## Estructura de ficheros
OrderBuilderDemo/
├── Order.java # Clase Product + Builder (Order y Order.Builder)
└── Main.java # Clase demo con método main()

text

## Requisitos
- JDK 8 o superior
- Línea de comandos

## Compilar
En la terminal desde el directorio OrderBuilderDemo/

Ejecutar:
```bash
javac Order.java Main.java

Ejecutar: 

java Main

Salida esperada

=== ORDEN COMPLETA ===
Order ID              : ORD-1001
Cliente               : Alice(CUST-42)
Items                 : [PROD-1 x2, PROD-7 x1]
Dirección envío       : Av. Central 123, San José 10101
Dirección facturación : Calle 9, Heredia 40101
Código descuento      : PROMO10
Empaque regalo        : Sí
Fecha pedido          : 2025-06-22T10:30

=== ORDEN SIMPLE ===
Order ID              : ORD-1002
Cliente               : Bob(CUST-99)
Items                 : [PROD-3 x1]
Dirección envío       : Calle 5, Alajuela 20101
Dirección facturación : [ninguno]
Código descuento      : [ninguno]
Empaque regalo        : No
Fecha pedido          : 2025-06-23T00:53:36.940854593
