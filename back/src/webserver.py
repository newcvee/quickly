from unicodedata import category
from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.dish import Dish
from src.domain.ingredients import Ingredients
from src.domain.categories import Categories


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"
    
    @app.route("/api/dishes", methods=["GET"])
    def dish_get():
        dishes = repositories["dishes"].get_dishes()
        return object_to_json(dishes)

    # @app.route("/api/alldishes/<category>", methods=["GET"])
    # def dish_get_all(category):
    #     all_dish = repositories["dishes"].get_dishes_by_category(category)
    #     return object_to_json(all_dish)
    
    @app.route("/api/dishes/<id>", methods=["GET"])
    def dish_get_by_id(id):
        dishes = repositories["dishes"].get_dishes_by_id(id)

        if id == dishes.id:
            return object_to_json(dishes), 200
        else:
            return "", 403

    @app.route("/api/category/dishes/<category_id>", methods=["GET"]) 
    def dish_get_by_category():
        dishes_by_category = repositories["dishes"].get_dishes_by_category()
        return object_to_json(dishes_by_category), 200

    
    @app.route("/api/ingredients", methods=["GET"])
    def ingredients_get():
        all_ingredients = repositories["ingredients"].get_ingredients()
        return object_to_json(all_ingredients), 200

    @app.route("/api/dish/ingredients/<dish_id>", methods=["GET"])
    def get_ingredients_by_dish(dish_id):
        dish_ingredients = repositories["ingredients"].get_ingredients_by_dish_id(dish_id)
        return object_to_json(dish_ingredients), 200

    @app.route("/api/categories", methods=["GET"])
    def categories_get():
        all_categories = repositories["categories"].get_categories()
        return object_to_json(all_categories), 200


    return app
