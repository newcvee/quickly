import sqlite3
from src.domain.item import Item, ItemsRepository


database_path = "data/database.db"


class Order:
    def __init__(self, order_id, order_date, order_price, order_state, order_items=None):
        self.order_id = order_id
        self.order_date = order_date
        self.order_price = order_price
        self.order_state = order_state
        if not order_items:
            order_items = ItemsRepository(database_path).get_order_items_by_event(id)
        self.order_items = order_items

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def to_dict(self):
        return {"order_id": self.order_id,
        "order_date": self.order_date,
        "order_price": self.order_price,
        "order_state": self.order_state,
        "order_items": self.order_items if self.order_items else [],
        }


class OrdersRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists orders (
                order_id VARCHAR PRIMARY KEY,
                order_date VARCHAR,
                order_price NUMERIC,
                order_state VARCHAR,
                order_items TEXT
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()


    def save_order(self, orders):
        sql = """insert into orders (order_id, order_date, order_price, order_state) values (
            :order_id, :order_date, :order_price, :order_state
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, orders.to_dict())
        conn.commit()

    def get_orders(self):
        sql="""select * from orders"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data= cursor.fetchall()
        result = []
        for item in data:
            order = Order(**item)
            result.append(order)
        return result

    