from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.dish import Dish


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)
    
    @app.route("/api/dishes", methods=["GET"])
    def dish_get():
        dish = repositories["dish"].get_dish()
        return object_to_json(dish)


    return app
