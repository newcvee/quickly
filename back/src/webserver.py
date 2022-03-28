from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.dish import Dish
from src.domain.ingredients import Ingredients


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"
    
    @app.route("/api/dishes", methods=["GET"])
    def dish_get():
        dish = repositories["dish"].get_dish()
        return object_to_json(dish)
    
    @app.route("/api/dishes/<id>", methods=["GET"])
    def dish_get_by_id(id):
        dish = repositories["dish"].get_dish_by_id(id)

        if id == dish.id:
            return object_to_json(dish), 200
        else:
            return "", 403
    
    @app.route("/api/ingredients", methods=["GET"])
    def ingredients_get():
        all_ingredients = repositories["ingredients"].get_ingredients()
        return object_to_json(all_ingredients), 200

    @app.route("/api/dish/ingredients/<dish_id>", methods=["GET"])
    def get_ingredients_by_dish(dish_id):
        dish_ingredients = repositories["ingredients"].get_ingredients_by_dish_id(dish_id)
        return object_to_json(dish_ingredients), 200


    return app
