import sqlite3
from src.webserver import create_app
from src.domain.dish import DishRepository
from src.domain.ingredients import IngredientsRepository
from src.domain.categories import CategoriesRepository


database_path = "data/database.db"

repositories = {
    "dish": DishRepository(database_path),
    "ingredients": IngredientsRepository(database_path),
    "categories": CategoriesRepository(database_path)
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
