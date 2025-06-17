from abc import ABC, abstractmethod

class ICookingSeasoning(ABC):
  @abstractmethod
  def add(self) -> str:
    """Añade una cantidad en gramos del condimento."""
    pass

  def get_seasonig_state(self) -> str:
    """Devuelve si ya se añadió el sazonador o no."""
    pass