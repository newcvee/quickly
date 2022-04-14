import sqlite3


class Order:
    def __init__(self, order_id, order_description):
        self.order_id = order_id
        self.order_description = order_description
    def to_dict(self):
        return {"order_id": self.order_id  ,
        "order_description": self.order_description}


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
                order_description VARCHAR
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()


    def save_order(self, orders):
        sql = """insert into orders (order_id, order_description) values (
            :order_id, :order_description
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, orders.to_dict())
        conn.commit()

        