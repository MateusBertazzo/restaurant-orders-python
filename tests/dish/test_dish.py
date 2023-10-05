from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    pizzaMozzarela = Dish("pizza de mozzarella", 50.00)
    pizzaMozzarela2 = Dish("pizza de mozzarella", 50.00)

    pastChicken = Dish("frango empanado", 25.00)

    assert pizzaMozzarela.name == "pizza de mozzarella"
    assert pizzaMozzarela.price == 50.00

    assert pizzaMozzarela.__repr__() == "Dish('pizza de mozzarella', R$50.00)"
    assert pizzaMozzarela2.__repr__() == "Dish('pizza de mozzarella', R$50.00)"
    assert pastChicken.__repr__() == "Dish('frango empanado', R$25.00)"

    assert pizzaMozzarela.__eq__(pizzaMozzarela2) is True
    assert pizzaMozzarela2.__eq__(pastChicken) is False
    assert pizzaMozzarela.__eq__(pastChicken) is False

    assert hash(pizzaMozzarela) == hash(pizzaMozzarela2)
    assert hash(pizzaMozzarela) != hash(pastChicken)
    assert hash(pizzaMozzarela2) != hash(pastChicken)

    pizzaMozzarela.add_ingredient_dependency(Ingredient("tomate"), 1)
    pizzaMozzarela.add_ingredient_dependency(Ingredient("Ketshup"), 5)
    pizzaMozzarela.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)

    assert pizzaMozzarela.get_ingredients() == {
        Ingredient("Ketshup"),
        Ingredient("tomate"),
        Ingredient("queijo mussarela"),
    }

    assert pizzaMozzarela.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }

    with pytest.raises(ValueError):
        Dish("pizza de mozzarella", 0)
    with pytest.raises(ValueError):
        Dish("pizza de mozzarella", -5)
    with pytest.raises(TypeError):
        Dish("pizza de mozzarella", "50.00")
