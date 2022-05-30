from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.orders import OrdersRepository, Order


def test_should_return_empty_list_of_orders():
    orders_repository = OrdersRepository(temp_file())
    app = create_app(repositories={"orders": orders_repository})
    client = app.test_client()

    response = client.get("/api/orders")

    assert response.json == []


def test_should_return_list_of_orders():
    orders_repository = OrdersRepository(temp_file())
    app = create_app(repositories={"orders": orders_repository})
    client = app.test_client()

 
    first_order = Order(order_id = "1_id",
        order_date= "21/22/2222",
        order_price = 999.99,
        order_state = "waiting",
        order_description = "Hey"
    )
    second_order = Order(order_id = "2_id",
        order_date= "21/22/2222",
        order_price = "999.99",
        order_state = "waiting",
        order_description = "Hey"
    )
   

    orders_repository.save_order(first_order)
    orders_repository.save_order(second_order)
    

    response = client.get("/api/orders")

    assert response.json == [
        {
            "order_id" : "1_id",
            "order_date": "21/22/2222",
            "order_price": 999.99,
            "order_state": "waiting",
            "order_description":"Hey"
        },
        {
            "order_id" : "2_id",
            "order_date": "21/22/2222",
            "order_price": 999.99,
            "order_state": "waiting",
            "order_description":"Hey"
        }
    ]

    
   
