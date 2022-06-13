import sqlite3


class Item:
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


class ItemsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql1 = """
            create table if not exists items (
                id VARCHAR PRIMARY KEY,
                name VARCHAR,
                img VARCHAR,
                price NUMERIC,
                category_id VARCHAR FOREING KEY 
                REFERENCES categories (category_id)
            );
            create table if not exists orderitems(
                order_id VARCHAR,
                id VARCHAR,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (id) REFERENCES items(id)
            )
            """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.executescript(sql1)
        conn.commit()
        conn.close()    


    def get_item(self):
        sql = """select * from items"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()
        
        return Item(id=data["id"],
        name = data["name"],
        img = data["img"],
        price = data["price"],
        category_id = data["category_id"])
    
    def get_items(self):
        sql = """select * from items"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        result = []
        for item in data:
            item = Item(**item)
            result.append(item)
        conn.close()
        return result


    def get_items_by_id(self, id):
        sql = """SELECT * FROM items WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()

        if data is not None:
            item = Item(**data)
        else:
            item = None
            
        return item
    
    def items_categories(self, category_id):
        sql = """SELECT items.id, items.name, items.img, items.price, items.category_id
        FROM items 
        INNER JOIN categories ON items.category_id = categories.category_id
        WHERE categories.category_id = :category_id
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"category_id": category_id})

        data = cursor.fetchall()
        result = []
        for item in data:
            items = Item(**item)
            result.append(items)
        
        return result
    
    def get_items_by_order(self, order_id):
        conn= self.create_conn()
        cursor = conn.cursor()
        sql_items = """SELECT *
            from orderitems, items 
            WHERE orderitems.id = items.id and order_id = :order_id"""
        cursor.execute(sql_items, {"order_id": order_id})
        items = cursor.fetchall()
        items = [Item(**item).to_dict() for item in items]
        conn.close()
        return items
    
    def save(self, items):
        sql = """insert into items (id, name, img, price, category_id) values (
            :id, :name, :img, :price, :category_id
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, items.to_dict())
        conn.commit()

    def save_order_items(self, order_id, order_items):
        conn = self.create_conn()
        cursor = conn.cursor()
        sql_order_items= """ INSERT into orderitems (order_id, id) VALUES (:order_id, :id) """

        print("******************************", order_items)
        
        print("******************************", order_id)

        for item in order_items:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!", item)
            item_id = item.get('id')
            cursor.execute(sql_order_items, {"order_id": order_id, "id": item_id})
        
        conn.commit()
        conn.close()