
import sys

sys.path.insert(0, "")

database_path = "data/database.db"

from src.domain.item import Item, ItemsRepository
from src.domain.ingredients import Ingredients, IngredientsRepository
from src.domain.categories import Categories, CategoriesRepository
from src.domain.orders import Order, OrdersRepository



items_repository = ItemsRepository(database_path)
ingredients_repository = IngredientsRepository(database_path)
categories_repository = CategoriesRepository(database_path)
orders_repository = OrdersRepository(database_path)



yakitori_cerdo_item= Item(id= "1",
name = "Yakitori de Cerdo con Especias Picantes",
img = "h7CEF3E4A60287C95",
price = 3.50,
category_id = "1"
)
yakitori_pollo_item= Item(id= "2",
name = "Yakitori de Pollo con Salsa Sukai",
img = "h7CEF3E4A60287C95",
price = 3.50,
category_id = "1"
)
yakitori_tofu_item= Item(id= "3",
name = "Yakitori de Tofu de Pescado ",
img = "h7CEF3E4A60287C95",
price = 3.50,
category_id = "1"
)
yakitori_vegetal_item= Item(id= "4",
name = "Yakitori Vegetal",
img = "h7CEF3E456541",
price = 3.50,
category_id = "1"
)
gyoza_ternera_item= Item(id= "5",
name = "Gyoza de Ternera al Curry",
img = "h7CEF3E445645",
price = 4.50,
category_id = "1"
)
gyoza_pollo_item= Item(id= "6",
name = "Gyoza de Pollo",
img = "h7CEF3E445645",
price = 3.95,
category_id = "1"
)
gyoza_verdura_item= Item(id= "7",
name = "Gyoza de Verdura",
img = "h7CEF3E445645",
price = 3.95,
category_id = "1"
)
alitas_nori_item= Item(id= "8",
name = "Alitas de Pollo con Alga Nori",
img = "h7CEF3E445645",
price = 5.85,
category_id = "1"
)
alitas_picantes_item= Item(id= "9",
name = "Alitas de Pollo Picantes",
img = "h7CEF3E445645",
price = 5.85,
category_id = "1"
)
rollito_pollo_item= Item(id= "10",
name = "Rollito de Pollo",
img = "h7CEF3E445645",
price = 2.50,
category_id = "1"
)
rollito_vegetal_item= Item(id= "11",
name = "Rollito Vegetal",
img = "h7CEF3E445645",
price = 1.80,
category_id = "1"
)



items_repository.save(yakitori_cerdo_item)
items_repository.save(yakitori_pollo_item)
items_repository.save(yakitori_tofu_item)
items_repository.save(yakitori_vegetal_item)
items_repository.save(gyoza_ternera_item)
items_repository.save(gyoza_pollo_item)
items_repository.save(gyoza_verdura_item)
items_repository.save(alitas_nori_item)
items_repository.save(alitas_picantes_item)
items_repository.save(rollito_pollo_item)
items_repository.save(rollito_vegetal_item)




ensalada_karaage_item= Item(id= "12",
name = "Ensalada de Karaage",
img = "h7CEF3E445645",
price = 4.95,
category_id = "2"
)
ensalada_ebi_item= Item(id= "13",
name = "Ensalada Ebi",
img = "h7CEF3E445645",
price = 4.95,
category_id = "2"
)
ensalada_salmon_item= Item(id= "14",
name = "Ensalada de Salmón Marinado",
img = "h7CEF3E445645",
price = 5.50,
category_id = "2"
)
ensalada_soba_item= Item(id= "15",
name = "Ensalada de Soba",
img = "h7CEF3E445645",
price = 4.95,
category_id = "2"
)



items_repository.save(ensalada_karaage_item)
items_repository.save(ensalada_ebi_item)
items_repository.save(ensalada_salmon_item)
items_repository.save(ensalada_soba_item)



arroz_cerdo_item= Item(id= "16",
name = "Arroz con Cerdo Marinado Estilo Japonés",
img = "h7CEF3E445645",
price = 7.85,
category_id = "3"
)
arroz_karaage_item= Item(id= "17",
name = "Arroz con Karaage",
img = "h7CEF3E445645",
price = 7.25,
category_id = "3"
)
arroz_ternera_item= Item(id= "18",
name = "Arroz con Ternera al Curry",
img = "h7CEF3E445645",
price = 7.50,
category_id = "3"
)
arroz_pato_item= Item(id= "19",
name = "Arroz con Pato Laqueado con Hoisin",
img = "h7CEF3E445645",
price = 8.25,
category_id = "3"
)
arroz_salmon_item= Item(id= "20",
name = "Arroz con Salmón con Salsa Teriyaki",
img = "h7CEF3E445645",
price = 8.25,
category_id = "3"
)
arroz_anguila_item= Item(id= "21",
name = "Arroz con Anguila con Salsa Teriyaki",
img = "h7CEF3E445645",
price = 8.95,
category_id = "3"
)
arroz_verduras_item= Item(id= "22",
name = "Arroz con Verduras",
img = "h7CEF3E445645",
price = 6.95,
category_id = "3"
)



items_repository.save(arroz_cerdo_item)
items_repository.save(arroz_karaage_item)
items_repository.save(arroz_ternera_item)
items_repository.save(arroz_pato_item)
items_repository.save(arroz_salmon_item)
items_repository.save(arroz_anguila_item)
items_repository.save(arroz_verduras_item)



yakisoba_cerdo_item= Item(id= "23",
name = "Yakisoba de Cerdo Marinado Estilo Japonés",
img = "h7CEF3E445645",
price = 7.50,
category_id = "4"
)
yakisoba_pollo_item= Item(id= "24",
name = "Yakisoba de Pollo Tempayaki",
img = "h7CEF3E445645",
price = 7.50,
category_id = "4"
)
yakisoba_pato_item= Item(id= "25",
name = "Yakisoba de Pato Salteado",
img = "h7CEF3E445645",
price = 8.25,
category_id = "4"
)
yakisoba_salmon_item= Item(id= "26",
name = "Yakisoba de Salmón Salteado",
img = "h7CEF3E445645",
price = 8.25,
category_id = "4"
)
yakisoba_ebi_item= Item(id= "27",
name = "Yakisoba de Ebi",
img = "h7CEF3E445645",
price = 7.95,
category_id = "4"
)
yakisoba_boletus_item= Item(id= "28",
name = "Yakisoba de Boletus",
img = "h7CEF3E445645",
price = 7.50,
category_id = "4"
)
yakisoba_vegetal_item= Item(id= "29",
name = "Yakisoba de Vegetal",
img = "h7CEF3E445645",
price = 6.95,
category_id = "4"
)


items_repository.save(yakisoba_cerdo_item)
items_repository.save(yakisoba_pollo_item)
items_repository.save(yakisoba_pato_item)
items_repository.save(yakisoba_salmon_item)
items_repository.save(yakisoba_ebi_item)
items_repository.save(yakisoba_boletus_item)
items_repository.save(yakisoba_vegetal_item)



ramen_cerdo_item= Item(id= "30",
name = "Ramen de Cerdo Marinado Estilo Japonés",
img = "h7CEF3E445645",
price = 8.50,
category_id = "5"
)
ramen_karaage_item= Item(id= "31",
name = "Ramen de Karaage",
img = "h7CEF3E445645",
price = 8.25,
category_id = "5"
)
ramen_pollo_item= Item(id= "32",
name = "Ramen de Pollo Tempayaki",
img = "h7CEF3E445645",
price = 8.25,
category_id = "5"
)
ramen_ternera_item= Item(id= "33",
name = "Ramen de Ternera",
img = "h7CEF3E445645",
price = 8.25,
category_id = "5"
)
ramen_pato_item= Item(id= "34",
name = "Ramen de Pato",
img = "h7CEF3E445645",
price = 8.95,
category_id = "5"
)
ramen_surimi_item= Item(id= "35",
name = "Ramen Surimi",
img = "h7CEF3E445645",
price = 7.50,
category_id = "5"
)
ramen_ebi_item= Item(id= "36",
name ="Ramen Ebi",
img = "h7CEF3E445645",
price = 8.50,
category_id = "5"
)
ramen_vegetal_item= Item(id= "37",
name ="Ramen Vegetal",
img = "h7CEF3E445645",
price = 7.50,
category_id = "5"
)


items_repository.save(ramen_cerdo_item)
items_repository.save(ramen_karaage_item)
items_repository.save(ramen_pollo_item)
items_repository.save(ramen_ternera_item)
items_repository.save(ramen_pato_item)
items_repository.save(ramen_surimi_item)
items_repository.save(ramen_ebi_item)
items_repository.save(ramen_vegetal_item)


salsa_soja_item= Item(id= "38",
name ="Salsa Soja",
img = "h7CEF3E445645",
price = 0.30,
category_id = "6"
)
salsa_agridulce_item= Item(id= "39",
name ="Salsa Agridulce",
img = "h7CEF3E445645",
price = 0.30,
category_id = "6"
)
salsa_picante_item= Item(id= "40",
name ="Salsa Picante",
img = "h7CEF3E445645",
price = 0.60,
category_id = "6"
)
salsa_teriyaki_item= Item(id= "41",
name ="Salsa Teriyaki",
img = "h7CEF3E445645",
price = 0.60,
category_id = "6"
)
salsa_hoisin_item= Item(id= "42",
name ="Salsa Hoisin",
img = "h7CEF3E445645",
price = 0.60,
category_id = "6"
)
aceite_picante_item= Item(id= "43",
name ="Aceite picante",
img = "h7CEF3E445645",
price = 0.60,
category_id = "6"
)


items_repository.save(salsa_soja_item)
items_repository.save(salsa_agridulce_item)
items_repository.save(salsa_picante_item)
items_repository.save(salsa_teriyaki_item)
items_repository.save(salsa_hoisin_item)
items_repository.save(aceite_picante_item)


bebida_cocalcola_item= Item(id= "45",
name ="Coca Cola, 50cl",
img = "h7CEF3E445645",
price = 2.30,
category_id = "7"
)
bebida_cocalcolacero_item= Item(id= "46",
name ="Coca Cola Zero, 50cl",
img = "h7CEF3E445645",
price = 2.30,
category_id = "7"
)
bebida_fantanaranja_item= Item(id= "47",
name ="Fanta Naranja, 50cl",
img = "h7CEF3E445645",
price = 2.30,
category_id = "7"
)
bebida_fantalimon_item= Item(id= "48",
name ="Fanta Limón, 50cl",
img = "h7CEF3E445645",
price = 2.30,
category_id = "7"
)
bebida_sprite_item= Item(id= "49",
name ="Sprite, 50cl",
img = "h7CEF3E445645",
price = 2.30,
category_id = "7"
)
bebida_nestea_item= Item(id= "50",
name ="Nestea, 50cl",
img = "h7CEF3E445645",
price = 2.30,
category_id = "7"
)

items_repository.save(bebida_cocalcola_item)
items_repository.save(bebida_cocalcolacero_item)
items_repository.save(bebida_fantanaranja_item)
items_repository.save(bebida_fantalimon_item)
items_repository.save(bebida_sprite_item)
items_repository.save(bebida_nestea_item)


first_dish_ingr_one= Ingredients( ingr_id= "1",
dish_id="1",
name= "tomato",
state="with")

first_dish_ingr_two= Ingredients( ingr_id= "2",
dish_id="1",
name= "letucce",
state="with")

first_dish_ingr_three= Ingredients( ingr_id= "3",
dish_id="1",
name= "cheese",
state="with")



ingredients_repository.save_ingr(first_dish_ingr_one)
ingredients_repository.save_ingr(first_dish_ingr_two)
ingredients_repository.save_ingr(first_dish_ingr_three)

entrantes_category = Categories(
    category_id = "1",
    name= "Entrantes",
    image= "hello"
)
ensaladas_category = Categories(
    category_id = "2",
    name= "Ensaladas",
    image= "hello"
)
arroz_category = Categories(
    category_id = "3",
    name= "Arroz",
    image= "hello"
)
yakisoba_category = Categories(
    category_id = "4",
    name= "Yakisoba",
    image= "hello"
)
ramen_category = Categories(
    category_id = "5",
    name= "Ramen",
    image= "hello"
)
salsas_category = Categories(
    category_id = "6",
    name= "Salsas",
    image= "hello"
)
bebidas_category = Categories(
    category_id = "7",
    name= "Bebidas",
    image= "hello"
)
categories_repository.save_category(entrantes_category)
categories_repository.save_category(ensaladas_category)
categories_repository.save_category(arroz_category)
categories_repository.save_category(yakisoba_category)
categories_repository.save_category(ramen_category)
categories_repository.save_category(salsas_category)
categories_repository.save_category(bebidas_category)






first_order = Order(order_id = "1_id",
    order_number = 1,
    order_date= "21/22/2222",
    order_price = 999.99,
    order_state = "waiting",
    order_items = [{
                "id" : "1",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            },{
                "id" : "3",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            }]
)
second_order = Order(order_id = "2_id",
    order_number = 2,
    order_date= "21/22/2222",
    order_price = 999.99,
    order_state = "waiting",
    order_items = [{
                "id" : "1",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            },{
                "id" : "3",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            }]
)
third_order = Order(order_id = "3_id",
        order_number = 3,
    order_date= "21/22/2222",
    order_price = 999.99,
    order_state = "doing",
    order_items = [{
                "id" : "1",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            },{
                "id" : "3",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            }]
)
fourth_order = Order(order_id = "4_id",
    order_number = 5,
    order_date= "21/22/2222",
    order_price = 999.99,
    order_state = "done",
    order_items = [{
                "id" : "1",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            },{
                "id" : "3",
                "name" : "test menu ",
                "img" : "h7CEF3E4A60287C95",
                "price" : 10.95,
                "category_id" : "3"   
            }]
)

orders_repository.save_order(first_order)
orders_repository.save_order(second_order)
orders_repository.save_order(third_order)
orders_repository.save_order(fourth_order)
