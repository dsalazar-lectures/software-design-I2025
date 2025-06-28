from i_build_house import BuildHouseInterface

# Esta clase construye como entrada principal una puerta de garaje
class BuildHouseWithGarageEntry(BuildHouseInterface):
  """
  Clase que construye una casa con garaje en la entrada.
  """

  def buildEntry(self):
    """Construye la entrada principal de la casa con garaje"""
    return "Construyendo la entrada principal de la casa con garaje"