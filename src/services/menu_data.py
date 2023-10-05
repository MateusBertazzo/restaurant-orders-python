# Req 3
from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path):
        self.dishes = []
        self.ingredients = {}
        self.load_data(source_path)

    # carrega os dados do csv
    def load_data(self, source_path):
        for row in self.read_csv(source_path):
            self.create_dish(row)

    # le o arquivo csv e retorna um iterador para as linhas
    def read_csv(self, source_path):
        return pd.read_csv(source_path).itertuples(index=False)

    # cria um prato e adiciona ao Conjunto de pratos
    def create_dish(self, dish_object):
        name, price, ingredient, quantity = dish_object
        price = float(price)

        existing_dish = next((d for d in self.dishes if d.name == name), None)

        if existing_dish is None:
            new_dish = Dish(name, price)
            self.dishes.append(new_dish)
        else:
            new_dish = existing_dish

        ingredient = Ingredient(ingredient)
        new_dish.add_ingredient_dependency(ingredient, int(quantity))
