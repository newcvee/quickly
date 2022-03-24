import sqlite3


class Dish:
    def __init__(self, dish_id, name, img):
        self.dish_id = dish_id
        self.name = name
        self.img = img

    def to_dict(self):
        return {"dish_id": self.dish_id,
        "name": self.name,
        "img": self.img}


class DishRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists dish (
                dish_id VARCHAR PRIMARY KEY,
                name VARCHAR,
                img VARCHAR
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_info(self):
        sql = """select * from dish"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()

        return Dish(dish_id=data["dish_id"],
        name = data["name"],
        img = data ["img"])

    def save(self, info):
        sql = """insert into info (dish_id, name, img) values (
            :dish_id, :name, :img
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, dish.to_dict())
        conn.commit()
