from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.dish import DishRepository, Dish

def test_front_should_post_new_dish():
    dishes_repository = DishRepository(temp_file())
    app = create_app(repositories={"dishes": dishes_repository})
    client = app.test_client()

    body = {
        "id" : "0015",
        "name" : "test menu ",
        "img" : "h7CEF3E4A60287C95",
        "price" : "10,95",
        "category_id" : "3"   
    }

    response_post = client.post("/api/dishes", json=body)
    assert response_post.status_code == 200

    response_get = client.get("/api/dishes/0015")
    assert response_get.status_code == 200
    assert response_get.json == {
        "id" : "0015",
        "name" : "test menu ",
        "img" : "h7CEF3E4A60287C95",
        "price" : "10,95",
        "category_id" : "3"
    }

