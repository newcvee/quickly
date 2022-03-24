
import sys

sys.path.insert(0, "")

from src.domain.info import Info, InfoRepository

database_path = "data/database.db"

info_repository = InfoRepository(database_path)

info_repository.save(Info(app_name="f5-seed-app"))
from src.domain.info import Info, InfoRepository
from src.domain.dish import Dish, DishRepository

database_path = "data/database.db"

info_repository = InfoRepository(database_path)
dish_repository = InfoRepository(database_path)

info_repository.save(Info(app_name="f5-seed-app"))

first_dish= Dish(dish_id= "burguer-1",
name = "burguer",
img = "https://www.bing.com/images/search?q=Burger&FORM=IQFRBA&id=EF2980334DB78C2CB72A7F857CEF3E4A60287C95",
)

dish_repository.save(first_dish)


