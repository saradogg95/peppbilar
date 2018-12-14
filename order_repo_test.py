from models.Order import Order
from repositories.OrderRepo import OrderRepository



order_db = OrderRepository()



""" get_order = order_db.get_order(1)
print(get_order)

get_order2 = order_db.get_order(5)
print(get_order2)

get_customer_orders = order_db.get_customer_orders(100)
if not get_customer_orders:
    print(get_customer_orders)
    print("blah") """

all_customer = order_db.get_all_orders()
print("All orders:")
for order in all_customer:
    print(order)