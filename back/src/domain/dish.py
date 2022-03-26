import sqlite3


class Dish:
    def __init__(self, id, name, img):
        self.id = id
        self.name = name
        self.img = img

    def to_dict(self):
        return {"id": self.id,
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
                id VARCHAR PRIMARY KEY,
                name VARCHAR,
                img VARCHAR
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_dish(self):
        sql = """select * from dish"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()

        return Dish(id=data["id"],
        name = data["name"],
        img = data ["img"])

    def get_dish_by_id(self, id):
        sql = """SELECT * FROM dish WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()

        if data is not None:
            dish = Dish(**data)
        else:
            dish = None
            
        return dish

    def save(self, dish):
        sql = """insert into dish (id, name, img) values (
            :id, :name, :img
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, dish.to_dict())
        conn.commit()
