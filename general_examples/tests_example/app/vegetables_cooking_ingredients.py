from tests_example.app.i_cooking_ingredients import ICookingIngredients

class VegetableIngredient(ICookingIngredients):
    def __init__(self, name : str, quantity : float, quality : str):
        self.name = name
        self.quantity = quantity
        self.quality = quality


    def get_name(self):
        return self.name 
    
    def get_quantity(self):
        return self.quantity
    
    def get_quality(self):
        return ("good" if self.quality == "fresh" else "bad")
        

