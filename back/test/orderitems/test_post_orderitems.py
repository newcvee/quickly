from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.item import Item, ItemsRepository


def test_front_should_post_in_orderitems():
    orderitems_repository = ItemsRepository(temp_file())
    app = create_app(repositories={"orderitems": orderitems_repository})
    client = app.test_client()

    body = {
            "order_id" : "16_id",
            "order_number" : "85",
            "order_date": "21/10/2022",
            "order_price": 999.99,
            "order_state": "waiting",
            "order_items": [{
                "id" : "1",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            },{
                "id" : "3",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            }]
        }
    
    orderitems_repository.save_order_items(body["order_id"], body["order_items"],)
    

    
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

