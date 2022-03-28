
import sys

sys.path.insert(0, "")

database_path = "data/database.db"

from src.domain.dish import Dish, DishRepository
from src.domain.ingredients import Ingredients, IngredientsRepository

dish_repository = DishRepository(database_path)
ingredients_repository = IngredientsRepository(database_path)



first_dish= Dish(id= "
1",
name = "burguer",
img = "https://www.bing.com/images/search?q=Burger&FORM=IQFRBA&id=EF2980334DB78C2CB72A7F857CEF3E4A60287C95",
)


first_dish_ingr_one= Ingredients( ingr_id= "1",
dish_id="1",
name= "tomato",
state="with")

first_dish_ingr_two= Ingredients( ingr_id= "2",
dish_id="1",
name= "letucce",
state="with")

first_dish_ingr_three= Ingredients( ingr_id= "3",
dish_id="1",
name= "cheese",
state="with")


dish_repository.save(first_dish)
ingredients_repository.save_ingr(first_dish_ingr_one)
ingredients_repository.save_ingr(first_dish_ingr_two)
ingredients_repository.save_ingr(first_dish_ingr_three)
