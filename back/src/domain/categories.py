import sqlite3


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

        data = cursor.fetchone()

        return Categories(category_id=data["category_id"],
        name = data["name"],)

    def save_category(self, categories):
        sql = """insert into categories (category_id,name, image) values (
            :category_id,:name, :image
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, categories.to_dict())
        conn.commit()

    # def get_ingredients_by_dish_id(self,dish_id):
    #     sql = """SELECT * FROM ingredients WHERE dish_id = :dish_id"""
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(sql, {"dish_id": dish_id})
    #     data = cursor.fetchall()
    #     result = []
    #     for item in data:
    #         ingredient = Ingredients(**item)
    #         result.append(ingredient)
        
    #     return result
    
    # def get_ingredients_by_dish_id(self, dish_id):
    #     sql = """SELECT * FROM dish WHERE dish_id=:dish_id"""
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(sql, {"dish_id": dish_id})

    #     data = cursor.fetchall()

    #     ingredients = [Ingredients(**item) for item in data]
    #     return ingredients
        
