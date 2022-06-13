from re import I
from unicodedata import category
from flask import Flask
from flask_cors import CORS
from flask import Flask, request, jsonify

from src.lib.utils import object_to_json
from src.domain.item import Item
from src.domain.categories import Categories
from src.domain.orders import Order


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"
    
    @app.route("/api/item", methods=["GET"])
    def item_get():
        items = repositories["items"].get_item()
        return object_to_json(items)
        
    @app.route("/api/items", methods=["GET"])
    def items_get():
        items = repositories["items"].get_items()
        return object_to_json(items)

    @app.route("/api/items", methods=["POST"])
    def items_post():
        data = request.json
        item = Item(id=data["id"],
            name = data["name"],
            img = data["img"],
            price = data["price"],
            category_id = data["category_id"])
        repositories["items"].save(item)
        return ""
    
    @app.route("/api/items/<id>", methods=["GET"])
    def item_get_by_id(id):
        items = repositories["items"].get_items_by_id(id)
        if id == items.id:
            return object_to_json(items), 200
        else:
            return "", 403
    
    @app.route("/api/category/items/<category_id>", methods=["GET"])
    def items_by_category(category_id):
        all_items_by_category = repositories["items"].items_categories(category_id)
        return object_to_json(all_items_by_category), 200
    
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
        data = request.json
        category = Categories(
            category_id=data["category_id"],
            name=data["name"],
            image=data["image"])
        repositories["categories"].save_category(category)
        return ""

    @app.route("/api/category/<category_id>", methods=["GET"])
    def category_get_by_id(category_id):
        categories = repositories["categories"].get_categories_by_id(category_id)
        if category_id == categories.category_id or categories != None:
            return object_to_json(categories), 200
        else:
            return "", 403

    @app.route("/api/orders", methods=["GET"])
    def orders_get():
        all_orders = repositories["orders"].get_orders()
        return object_to_json(all_orders), 200


    @app.route("/api/orders", methods=["POST"])
    def orders_post():
        data = request.json
        # print("********************************", data)
        order = Order(**data)
        order_items = data["order_items"]
        order_id = data["order_id"]
        # order_items_list = []
        # for item in order_items:
        #     order_items_list.append(item["id"])
        # print("<<<<<<<<<<<<<<<<<<", order_items_list)
        
        repositories["orders"].save_order(order)
        repositories["items"].save_order_items(order_id, order_items)

        return "", 200
        
    
    @app.route("/api/orders/<order_id>", methods=["GET"])
    def order_get_by_id(order_id):
        order = repositories["orders"].get_order_by_id(order_id)
        return object_to_json(order), 200
    
    @app.route("/api/categories/<category_id>", methods=["PUT"])
    def category_modify(category_id):
        data = request.json
        category = Categories(**data)
        repositories["categories"].modify_category(category_id, category)

        return ("", 200)
        
    @app.route("/api/items/<id>", methods=["PUT"])
    def item_modify(id):
        data = request.json
        item = Item(**data)
        repositories["items"].modify_category(id, item)
        return ("", 200)

    
    

    return app
