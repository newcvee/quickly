from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.item import Item, ItemsRepository
from src.domain.orders import OrdersRepository, Order


def test_front_should_post_in_orderitems():
    orderitems_repository = ItemsRepository(temp_file())
    orders_repository = OrdersRepository(temp_file())
    app = create_app(repositories={"items": orderitems_repository , "orders": orders_repository})
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
    
    response_post = client.post("/api/orders", json=body)
    assert response_post.status_code == 200
    
    response_get = client.get("/api/orders/16_id")
    assert response_get.status_code == 200

    assert response_get.json == {
            "order_id" : "16_id",
            "order_number" : "85",
            "order_date": "21/10/2022",
            "order_price": 999.99,
            "order_state": "waiting",
            "order_items": []
        }
    
    
    response_orderitem_get = client.get("/api/orders/orderitems/16_id")
    assert response_orderitem_get.status_code == 200
    assert response_orderitem_get.json == [
        {"order_id": 16_1, "id": 1},
        {"order_id": 16_1, "id": 3}
    ]

