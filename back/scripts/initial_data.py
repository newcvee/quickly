
import sys

sys.path.insert(0, "")

database_path = "data/database.db"

from src.domain.item import Item, ItemsRepository
from src.domain.categories import Categories, CategoriesRepository
from src.domain.orders import Order, OrdersRepository



items_repository = ItemsRepository(database_path)
categories_repository = CategoriesRepository(database_path)
orders_repository = OrdersRepository(database_path)



first_item= Item(id= "1",
name = "burguer",
img = "h7CEF3E4A60287C95",
price = "10,95",
category_id = "2"
)
second_item= Item(id= "2",
name = "milkshake",
img = "h7CEF3E4A60287C95",
price = "10,95",
category_id = "1"
)

third_item= Item(id= "3",
name = "burguer + milkshake ",
img = "h7CEF3E4A60287C95",
price = "10,95",
category_id = "3"
)
fourth_item= Item(id= "4",
name = "taco",
img = "h7CEF3E456541",
price = "10,95",
category_id = "2"
)
fifth_item= Item(id= "5",
name = "chicken burrito",
img = "h7CEF3E445645",
price = "10,95",
category_id = "2"
)
sixth_item= Item(id= "6",
name = "sandwitch",
img = "h7CEF3E4789789",
price = "10,95",
category_id = "2"
)

items_repository.save(first_item)
items_repository.save(second_item)
items_repository.save(third_item)
items_repository.save(fourth_item)
items_repository.save(fifth_item)
items_repository.save(sixth_item)


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
    order_description = "{'dish': 'taco','price': '10.95','date': '14-01-2022'}",
    order_status = "doing"
)
second_order = Order(
    order_id = "second_order",
    order_description = "{'dish': 'taco','price': '10.95','date': '14-01-2022'}",
    order_status = "doing"
)
third_order = Order(
    order_id = "third_order",
    order_description = "{'dish': 'taco','price': '10.95','date': '14-01-2022'}",
    order_status = "done"
)
fourth_order = Order(
    order_id = "fourth_order",
    order_description = "{'dish': 'taco','price': '10.95','date': '14-01-2022'}",
    order_status = "incoming"
)

orders_repository.save_order(first_order)
orders_repository.save_order(second_order)
orders_repository.save_order(third_order)
orders_repository.save_order(fourth_order)
