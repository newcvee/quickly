import sqlite3


class Ingredients:
    def __init__(self, ingr_id, dish_id, name, state):
        self.ingr_id = ingr_id
        self.dish_id = dish_id
        self.name = name
        self.state = state

    def to_dict(self):
        return {"ingr_id": self.ingr_id,
        "dish_id": self.dish_id,
        "name": self.name,
        "state": self.state}


class IngredientsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists ingredients (
                ingr_id VARCHAR PRIMARY KEY,
                dish_id TEXT,
                name VARCHAR,
                state VARCHAR
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_ingredients(self):
        sql = """select * from ingredients"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()

        return Ingredients(ingr_id=data["ingr_id"],
        dish_id=data["dish_id"],
        name = data["name"],
        state = data ["state"])

    def save_ingr(self, ingredients):
        sql = """insert into ingredients (ingr_id, dish_id, name, state) values (
            :ingr_id, :dish_id, :name, :state
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, ingredients.to_dict())
        conn.commit()

    def get_ingredients_by_dish_id(self,dish_id):
        sql = """SELECT * FROM ingredients WHERE dish_id = :dish_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"dish_id": dish_id})
        data = cursor.fetchall()
        result = []
        for item in data:
            ingredient = Ingredients(**item)
            result.append(ingredient)
        
        return result
    
    # def get_ingredients_by_dish_id(self, dish_id):
    #     sql = """SELECT * FROM dish WHERE dish_id=:dish_id"""
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(sql, {"dish_id": dish_id})

    #     data = cursor.fetchall()

    #     ingredients = [Ingredients(**item) for item in data]
    #     return ingredients
        
