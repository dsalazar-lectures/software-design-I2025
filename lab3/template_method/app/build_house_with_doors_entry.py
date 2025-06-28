from i_build_house import BuildHouseInterface

# Esta clase construye como entrada principal una puerta corriente
class BuildHouseWithDoorsEntry(BuildHouseInterface):
  """
  Clase que construye una casa con puertas en la entrada.
  """
  
  def buildEntry(self):
    """Construye la entrada principal de la casa con puertas"""
    return "Construyendo la entrada principal de la casa con puertas"
