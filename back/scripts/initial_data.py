
import sys

sys.path.insert(0, "")

database_path = "data/database.db"

from src.domain.dish import Dish, DishRepository
from src.domain.ingredients import Ingredients, IngredientsRepository
from src.domain.categories import Categories, CategoriesRepository


dish_repository = DishRepository(database_path)
ingredients_repository = IngredientsRepository(database_path)
categories_repository = CategoriesRepository(database_path)



first_dish= Dish(id= "1",
name = "burguer",
img = "h7CEF3E4A60287C95",
category_id = "2"
)
second_dish= Dish(id= "2",
name = "milkshake",
img = "h7CEF3E4A60287C95",
category_id = "1"
)
third_dish= Dish(id= "3",
name = "burguer + milkshake + ",
img = "h7CEF3E4A60287C95",
category_id = "3"
)

dish_repository.save(first_dish)
dish_repository.save(second_dish)
dish_repository.save(third_dish)

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



ingredients_repository.save_ingr(first_dish_ingr_one)
ingredients_repository.save_ingr(first_dish_ingr_two)
ingredients_repository.save_ingr(first_dish_ingr_three)

first_category = Categories(
    category_id = "1",
    name= "Drinks",
    image= "hello"
)
second_category = Categories(
    category_id = "2",
    name= "Dishes",
    image= "hello"
)
third_category = Categories(
    category_id = "3",
    name= "Menus",
    image= "hello"
)

categories_repository.save_category(first_category)
categories_repository.save_category(second_category)
categories_repository.save_category(third_category)