import sqlite3
from src.webserver import create_app
from src.domain.item import ItemsRepository
from src.domain.ingredients import IngredientsRepository
from src.domain.categories import CategoriesRepository
from src.domain.orders import OrdersRepository



database_path = "data/database.db"

repositories = {
    "items": ItemsRepository(database_path),
    "ingredients": IngredientsRepository(database_path),
    "categories": CategoriesRepository(database_path),
    "orders" : OrdersRepository(database_path),
    "orderitems" : ItemsRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
