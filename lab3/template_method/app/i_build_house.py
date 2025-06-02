from abc import ABC, abstractmethod

# Clase abstracta dónde se define el método plantilla (Template Method)
class BuildHouseInterface(ABC):
  """
  Clase abstracta que construye una casa por pasos.
  Uso del patrón template method
  """

  def buildWalls(self):
    """Construye las paredes de la casa"""
    return "Construyendo las paredes lisas de la casa"
  
  # Método que debe ser implementado por las subclases
  @abstractmethod
  def buildEntry(self):
    """Construye la entrada principal de la casa"""
    pass

  def buildWindows(self):
    """Instala las ventanas de la casa"""
    return "Instalando las ventanas de la casa"

  def buildRoof(self):
    """Construye el techo de la casa"""
    return "Construyendo el techo trianguar de la casa"

  def buildHouse(self):
    """Método plantilla que construye la casa"""
    steps = []
    steps.append(self.buildWalls())
    steps.append(self.buildEntry())
    steps.append(self.buildWindows())
    steps.append(self.buildRoof())
    return steps
      