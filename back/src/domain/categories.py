import sqlite3
from unicodedata import category


class Categories:
    def __init__(self, category_id, name, image):
        self.category_id = category_id
        self.name = name
        self.image = image

    def to_dict(self):
        return {"category_id": self.category_id,
        "name": self.name,
        "image" : self.image}


class CategoriesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists categories (
                category_id VARCHAR PRIMARY KEY,
                name VARCHAR,
                image VARCHAR
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_categories(self):
        sql = """select * from categories"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            category = Categories(**item)
            result.append(category)
        
        return result

    def get_categories_by_id(self, category_id):
        sql = """SELECT * FROM categories WHERE category_id=:category_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"category_id": category_id})

        data = cursor.fetchone()

        if data is not None:
            categories = Categories(**data)
        else:
            categories = None
            
        return categories
    
    def get_the_categories(self):
        sql = """SELECT categories.category_id,categories.name, categories.image, dishes.category_id
        FROM categories
        INNER JOIN dishes ON categories.category_id = dishes.category_id
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            dishes = Categories(**item)
            result.append(dishes)
        
        return result

       
    def save_category(self, categories):
        sql = """insert into categories (category_id,name, image) values (
            :category_id,:name, :image
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql,{"category_id":categories.category_id,"name":categories.name,"image":categories.image} )
        conn.commit()


    
    def modify_category(self, category_id, categories):
        sql = """
            UPDATE categories
            SET category_id= :category_id, name= :name, image= :image
            WHERE category_id = :category_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        params = categories.to_dict()
        params["category_id"] = category_id
        cursor.execute(sql, params)
        conn.commit()
        conn.close()


