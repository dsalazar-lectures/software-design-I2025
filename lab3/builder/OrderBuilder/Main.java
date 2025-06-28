import java.time.LocalDateTime;
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        // Pedido completo
        Order fullOrder = new Order.Builder("ORD-1001",
                                new Order.Customer("CUST-42", "Alice"))
            .addItem("PROD-1", 2)
            .addItem("PROD-7", 1)
            .withShippingAddress("Av. Central 123", "San José", "10101")
            .withBillingAddress("Calle 9", "Heredia", "40101")
            .withDiscountCode("PROMO10")
            .enableGiftWrap()
            .withOrderDate(LocalDateTime.of(2025, 6, 22, 10, 30))
            .build();

        // Pedido mínimo (solo lo obligatorio)
        Order simpleOrder = new Order.Builder("ORD-1002",
                                 new Order.Customer("CUST-99", "Bob"))
            .addItem("PROD-3", 1)
            .withShippingAddress("Calle 5", "Alajuela", "20101")
            .build();

        System.out.println("=== ORDEN COMPLETA ===");
        printOrder(fullOrder);

        System.out.println("\n=== ORDEN SIMPLE ===");
        printOrder(simpleOrder);
    }

    private static void printOrder(Order o) {
        System.out.println("Order ID              : " + o.getOrderId());
        System.out.println("Cliente               : " + o.getCustomer());
        System.out.println("Items                 : " + o.getItems());
        System.out.println("Dirección envío       : " + o.getShippingAddress());
        // billingAddress como String opcional
        String billing = Optional.ofNullable(o.getBillingAddress())
                                 .map(Object::toString)
                                 .orElse("[ninguno]");
        System.out.println("Dirección facturación : " + billing);
        String discount = Optional.ofNullable(o.getDiscountCode())
                                  .orElse("[ninguno]");
        System.out.println("Código descuento      : " + discount);
        System.out.println("Empaque regalo        : " + (o.isGiftWrap() ? "Sí" : "No"));
        System.out.println("Fecha pedido          : " + o.getOrderDate());
    }
}
