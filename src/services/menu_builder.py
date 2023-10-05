from services.inventory_control import InventoryMapping
from services.menu_data import MenuData


DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None):
        eligible_dishes = []

        # itera sobre todos os pratos
        for dish in self.menu_data.dishes:

            # verifica se o prato é elegivel
            is_true = (
                (
                    restriction is None or restriction not in
                    dish.get_restrictions())
                and all(
                    ingredient in self.inventory.inventory
                    for ingredient in
                    dish.get_ingredients())
            )

            # se for true cria dict com os dados do prato
            if is_true:
                dish_data = {
                    "dish_name": dish.name,
                    "price": dish.price,
                    "ingredients": dish.get_ingredients(),
                    "restrictions": dish.get_restrictions(),
                }

                eligible_dishes.append(dish_data)

        return eligible_dishes
