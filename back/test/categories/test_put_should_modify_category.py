from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.categories import CategoriesRepository, Categories


def test_should_modify_category():
    categories_repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": categories_repository})
    client = app.test_client()

    concierto_queen = Category(
        id="event-1",
        user_id="user-1",
        name="concierto queen",
        description="un tributo a queen",
        date="2022-01-25",
        public=0,
        time="22:00:00",
        categories=["category-1"],
    )

    events_repository.save(concierto_queen, "user-1")

    body = {
        "id": "event-1",
        "name": "concierto queen",
        "description": "un tributo a queen de la ostia",
        "date": "2022-01-25",
        "public": 1,
        "time": "22:00:00",
        "categories": [],  # estaba:  "category-1"
    }

    response = client.put(
        "/api/events/event-1", json=body, headers={"Authorization": "user-1"}
    )
    assert response.status_code == 200

    response_get = client.get("api/events/event-1", headers={"Authorization": "user-1"})

    assert response_get.json == {
        "id": "event-1",
        "user_id": "user-1",
        "name": "concierto queen",
        "description": "un tributo a queen de la ostia",
        "date": "2022-01-25",
        "public": 1,
        "time": "22:00:00",
        "categories": [],  # estaba: "category-1"
    }
