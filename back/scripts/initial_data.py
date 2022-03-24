
import sys

sys.path.insert(0, "")

database_path = "data/database.db"

from src.domain.dish import Dish, DishRepository

dish_repository = DishRepository(database_path)



first_dish= Dish(dish_id= "burguer-1",
name = "burguer",
img = "https://www.bing.com/images/search?q=Burger&FORM=IQFRBA&id=EF2980334DB78C2CB72A7F857CEF3E4A60287C95",
)

dish_repository.save(first_dish)


