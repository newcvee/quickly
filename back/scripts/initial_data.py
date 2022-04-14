
import sys

sys.path.insert(0, "")

database_path = "data/database.db"

from src.domain.dish import Dish, DishRepository
from src.domain.ingredients import Ingredients, IngredientsRepository
from src.domain.categories import Categories, CategoriesRepository
from src.domain.orders import Order, OrdersRepository



dish_repository = DishRepository(database_path)
ingredients_repository = IngredientsRepository(database_path)
categories_repository = CategoriesRepository(database_path)
orders_repository = OrdersRepository(database_path)



first_dish= Dish(id= "1",
name = "burguer",
img = "h7CEF3E4A60287C95",
price = "10,95",
category_id = "2"
)
second_dish= Dish(id= "2",
name = "milkshake",
img = "h7CEF3E4A60287C95",
price = "10,95",
category_id = "1"
)

third_dish= Dish(id= "3",
name = "burguer + milkshake ",
img = "h7CEF3E4A60287C95",
price = "10,95",
category_id = "3"
)
fourth_dish= Dish(id= "4",
name = "taco",
img = "h7CEF3E456541",
price = "10,95",
category_id = "2"
)
fifth_dish= Dish(id= "5",
name = "chicken burrito",
img = "h7CEF3E445645",
price = "10,95",
category_id = "2"
)
sixth_dish= Dish(id= "6",
name = "sandwitch",
img = "h7CEF3E4789789",
price = "10,95",
category_id = "2"
)

dish_repository.save(first_dish)
dish_repository.save(second_dish)
dish_repository.save(third_dish)
dish_repository.save(fourth_dish)
dish_repository.save(fifth_dish)
dish_repository.save(sixth_dish)

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


first_order = Order(
    order_id = "first_order",
    item_id = "5"  ,
    item_name = "taco bell"  ,
    item_price = "10.95"  
)

orders_repository.save_order(first_order)