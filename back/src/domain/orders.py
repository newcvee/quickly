import sqlite3
from unittest import result


class Order:
    def __init__(self, order_id, order_description, order_status):
        self.order_id = order_id
        self.order_description = order_description
        self.order_status = order_status
    def to_dict(self):
        return {"order_id": self.order_id  ,
        "order_description": self.order_description,
        "order_status": self.order_status}


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
                order_description VARCHAR,
                order_status VARCHAR
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()


    def save_order(self, orders):
        sql = """insert into orders (order_id, order_description, order_status) values (
            :order_id, :order_description, :order_status
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

    