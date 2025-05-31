from tests_example.app.i_cooking_seasoning import ICookingSeasoning

class DummySeasoning(ICookingSeasoning):
  def __init__(self, amount: float):
    self.added = False
    self.amount = amount

  def add(self):
    self.added = True
    return f"added {self.amount} grams of Dummy seasoning"

  def get_seasonig_state(self):
    return "added" if self.added else "no added"