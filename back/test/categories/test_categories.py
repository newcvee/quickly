from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.categories import CategoriesRepository, Categories


def test_should_return_empty_list_of_categories():
    categories_repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": categories_repository})
    client = app.test_client()

    response = client.get("/api/categories")

    assert response.json == []


def test_should_return_list_of_categories():

    # ARRANGE (given)

    categories_repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": categories_repository})
    client = app.test_client()

    first_category = Categories(
    category_id = "1",
    name= "Drinks",
    image= "hello"
    )
    second_category = Categories(
        category_id = "2",
        name= "Dishes",
        image= "hello"
    )
    third_category = Categories(
        category_id = "3",
        name= "Menus",
        image= "hello"
    )
    categories_repository.save_category(first_category)
    categories_repository.save_category(second_category)
    categories_repository.save_category(third_category)


    # ACT (when)
    response = client.get("/api/categories")

    # ASSERT (then)
    assert response.json == [
        {
            "category_id" : "1",
            "name": "Drinks",
            "image": "hello"
        },
        {
            "category_id" : "2",
            "name": "Dishes",
            "image": "hello"
        },
        {
            "category_id" : "3",
            "name": "Menus",
            "image": "hello"
        },
    ]

    
   
