import sqlite3
from unicodedata import category, name


class Dish:
    def __init__(self, id, name, img, price, category_id):
        self.id = id
        self.name = name
        self.img = img
        self.price = price
        self.category_id = category_id

    def to_dict(self):
        return {"id": self.id,
        "name": self.name,
        "img": self.img,
        "price": self.price,
        "category_id": self.category_id}


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
            create table if not exists dishes (
                id VARCHAR PRIMARY KEY,
                name VARCHAR,
                img VARCHAR,
                price VARCHAR,
                category_id NUMERIC FOREING KEY 
                REFERENCES categories (category_id)
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_dishes(self):
        sql = """select * from dishes"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()

        return Dish(id=data["id"],
        name = data["name"],
        img = data["img"],
        price = data["price"],
        category_id = data["category_id"])

    def get_dishes_by_id(self, id):
        sql = """SELECT * FROM dishes WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()

        if data is not None:
            dishes = Dish(**data)
        else:
            dishes = None
            
        return dishes
    
    def dishes_categories(self, category_id):
        sql = """SELECT dishes.id, dishes.name, dishes.img, dishes.price, dishes.category_id
        FROM dishes 
        INNER JOIN categories ON dishes.category_id = categories.category_id
        WHERE categories.category_id = :category_id
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"category_id": category_id})

        data = cursor.fetchall()
        result = []
        for item in data:
            dishes = Dish(**item)
            result.append(dishes)
        
        return result
    
    def save(self, dishes):
        sql = """insert into dishes (id, name, img, price, category_id) values (
            :id, :name, :img, :price, :category_id
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, dishes.to_dict())
        conn.commit()

        