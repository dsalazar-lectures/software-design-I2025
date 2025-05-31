from tests_example.app.i_cooking_seasoning import ICookingSeasoning

class SaltSeasoning(ICookingSeasoning):
  def __init__(self, amount: float):
    """
    amount: Cantidad a añadir del sazonador
    """
    print("SaltSeasoning initialized")
    self.amount = amount
    self.state = "not added"

  def add(self):
    print(f"Added {self.amount} grams of salt")
    self.state = "added"

  def get_seasonig_state(self):
    print("Getting seasoning state from the salt")
    return self.state