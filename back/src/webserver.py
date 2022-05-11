from re import I
from unicodedata import category
from flask import Flask
from flask_cors import CORS
from flask import Flask, request, jsonify

from src.lib.utils import object_to_json
from src.domain.dish import Dish
from src.domain.ingredients import Ingredients
from src.domain.categories import Categories
from src.domain.orders import Order


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
    
    @app.route("/api/dishes/<id>", methods=["GET"])
    def dish_get_by_id(id):
        dishes = repositories["dishes"].get_dishes_by_id(id)
        if id == dishes.id:
            return object_to_json(dishes), 200
        else:
            return "", 403
    
    @app.route("/api/category/dishes/<category_id>", methods=["GET"])
    def dishes_by_category(category_id):
        all_dishes_by_category = repositories["dishes"].dishes_categories(category_id)
        return object_to_json(all_dishes_by_category), 200
    
    @app.route("/api/allcategories", methods=["GET"])
    def all_categories():
        all_categories = repositories["categories"].get_the_categories()
        return object_to_json(all_categories), 200

    
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

    @app.route("/api/categories", methods=["POST"])
    def categories_post():
        body = request.json
        order = Order(
            category_id=body["category_id"],
            name=body["name"],
            image= body["image"]
        )
        repositories["categories"].save_category(category)

        return ""
    
    @app.route("/api/orders", methods=["GET"])
    def orders_get():
        all_orders = repositories["orders"].get_orders()
        return object_to_json(all_orders), 200

    @app.route("/api/orders", methods=["POST"])
    def orders_post():
        body = request.json
        order = Order(
            order_id=body["order_id"],
            order_description=body["order_description"],
        )
        repositories["orders"].save_order(order)

        return ""
    
    

    return app
