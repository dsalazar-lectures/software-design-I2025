import java.time.LocalDateTime;
import java.util.*;

public class Order {
    // Campos del Pedido
    private final String orderId;
    private final Customer customer;
    private final List<OrderItem> items;
    private final Address shippingAddress;
    private final Address billingAddress;
    private final String discountCode;
    private final boolean giftWrap;
    private final LocalDateTime orderDate;

    // Constructor privado
    private Order(Builder b) {
        this.orderId         = b.orderId;
        this.customer        = b.customer;
        this.items           = Collections.unmodifiableList(b.items);
        this.shippingAddress = b.shippingAddress;
        this.billingAddress  = b.billingAddress;
        this.discountCode    = b.discountCode;
        this.giftWrap        = b.giftWrap;
        this.orderDate       = b.orderDate;
    }
    public String getOrderId()            { return orderId; }
    public Customer getCustomer()         { return customer; }
    public List<OrderItem> getItems()     { return items; }
    public Address getShippingAddress()   { return shippingAddress; }
    public Address getBillingAddress()    { return billingAddress; }
    public String getDiscountCode()       { return discountCode; }
    public boolean isGiftWrap()           { return giftWrap; }
    public LocalDateTime getOrderDate()   { return orderDate; }

    @Override
    public String toString() {
        return "Order{" +
               "id=" + orderId +
               ", customer=" + customer +
               ", items=" + items +
               ", shipTo=" + shippingAddress +
               ", billTo=" + billingAddress +
               ", discount=" + discountCode +
               ", giftWrap=" + giftWrap +
               ", date=" + orderDate +
               '}';
    }

    // ——— Builder ———
    public static class Builder {
        // Obligatorios
        private final String orderId;
        private final Customer customer;
        // Opcionales con valores por defecto
        private List<OrderItem> items = new ArrayList<>();
        private Address shippingAddress = null;
        private Address billingAddress  = null;
        private String discountCode      = null;
        private boolean giftWrap         = false;
        private LocalDateTime orderDate  = LocalDateTime.now();

        public Builder(String orderId, Customer customer) {
            this.orderId  = orderId;
            this.customer = customer;
        }

        public Builder addItem(String productId, int quantity) {
            this.items.add(new OrderItem(productId, quantity));
            return this;
        }

        public Builder withShippingAddress(String street, String city, String zip) {
            this.shippingAddress = new Address(street, city, zip);
            return this;
        }

        public Builder withBillingAddress(String street, String city, String zip) {
            this.billingAddress = new Address(street, city, zip);
            return this;
        }

        public Builder withDiscountCode(String code) {
            this.discountCode = code;
            return this;
        }

        public Builder enableGiftWrap() {
            this.giftWrap = true;
            return this;
        }

        public Builder withOrderDate(LocalDateTime date) {
            this.orderDate = date;
            return this;
        }

        public Order build() {
            // Validaciones básicas
            if (items.isEmpty()) {
                throw new IllegalStateException("Un pedido debe tener al menos un ítem.");
            }
            if (shippingAddress == null) {
                throw new IllegalStateException("Debe especificar dirección de envío.");
            }
            return new Order(this);
        }
    }

    // Clases de apoyo
    public static class Customer {
        private final String id;
        private final String name;
        public Customer(String id, String name) { this.id = id; this.name = name; }
        @Override public String toString() { return name + "("+id+")"; }
    }

    public static class OrderItem {
        private final String productId;
        private final int quantity;
        public OrderItem(String pid, int qty) { this.productId = pid; this.quantity = qty; }
        @Override public String toString() { return productId+" x"+quantity; }
    }

    public static class Address {
        private final String street, city, zip;
        public Address(String s, String c, String z) { this.street=s; this.city=c; this.zip=z; }
        @Override public String toString() { return street+", "+city+" "+zip; }
    }
}
