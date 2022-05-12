from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.categories import CategoriesRepository, Categories

def test_front_should_post_new_category():
    categories_repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": categories_repository})
    client = app.test_client()

    body = {
        "category_id": "0014",
        "name": "sweets",
        "image": "un tributo a queen"   
    }

    response_post = client.post("/api/categories", json=body)
    assert response_post.status_code == 200

    response_get = client.get("/api/category/0014")
    assert response_get.status_code == 200
    assert response_get.json == {
        "category_id": "0014",
        "name": "sweets",
        "image": "un tributo a queen" 
    }

