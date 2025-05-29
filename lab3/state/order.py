from abc import ABC, abstractmethod

# Interface State
class OrderState(ABC):
  @abstractmethod
  def process(self, order):
    pass

  @abstractmethod
  def cancel(self, order):
    pass


# Pendiente
class PendingState(OrderState):
  def process(self, order):
    print("Procesando pedido...")
    order.state = ProcessingState()
  
  def cancel(self, order):
    print("Pedido cancelado")
    order.state = CanceledState()


# Procesando
class ProcessingState(OrderState):
  def process(self, order):
    print("Enviando a destinatario")
    order.state = ShippedState()
  
  def cancel(self, order):
    print("Cancelación no permitida en proceso")


# Enviado
class ShippedState(OrderState):
  def process(self, order):
    print("Pedido ya enviado")
  
  def cancel(self, order):
    print("Cancelación no permitida después de envío")


# Cancelado
class CanceledState(OrderState):
  def process(self, order):
    print("Pedido cancelado, no procesable")
  
  def cancel(self, order):
    print("Pedido ya cancelado")


# Contexto
class Order:
  def __init__(self):
    self.state = PendingState()
  
  def process(self):
    self.state.process(self)
  
  def cancel(self):
    self.state.cancel(self)


# Demo
if __name__ == "__main__":
  order = Order()
  order.process()  # Procesando -> Estado: Processing
  order.process()  # Enviando -> Estado: Shipped
  order.cancel()   # Error: Cancelación no permitida