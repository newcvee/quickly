from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.item import Item, ItemsRepository


def test_front_should_post_new_item():
    item_repository = ItemsRepository(temp_file())
    app = create_app(repositories={"items": item_repository})
    client = app.test_client()

    body = {
        "id" : "15",
        "name" : "test menu ",
        "img" : "h7CEF3E4A60287C95",
        "price" : 10.95,
        "category_id" : "3"   
    }

    response_post = client.post("/api/items", json=body)
    assert response_post.status_code == 200

    response_get = client.get("/api/items/15")
    assert response_get.status_code == 200
    assert response_get.json == {
        "id" : "15",
        "name" : "test menu ",
        "img" : "h7CEF3E4A60287C95",
        "price" : 10.95,
        "category_id" : "3"
    }

