from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 1
def test_ingredient():
    ingredientTomato = Ingredient("tomato")
    ingredientTomato2 = Ingredient("tomato")
    assert ingredientTomato.name == "tomato"
    assert hash(ingredientTomato) == hash(Ingredient("tomato"))
    assert ingredientTomato.__repr__() == "Ingredient('tomato')"

    ingredientMozzarella = Ingredient("queijo mussarela")
    assert ingredientMozzarella.name == "queijo mussarela"
    assert hash(ingredientMozzarella) == hash(Ingredient("queijo mussarela"))
    assert ingredientMozzarella.__repr__() == "Ingredient('queijo mussarela')"

    assert hash(ingredientTomato) != hash(ingredientMozzarella)
    assert ingredientTomato != ingredientMozzarella
    assert ingredientTomato == ingredientTomato2

    assert ingredientMozzarella.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
