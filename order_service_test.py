from models.Order import Order
from services.OrderServices import OrderServices

order_service = OrderServices()

new_order = Order("3","20181208" ,"20180302","20180302","400","GL302")
order_service.add_order(new_order)
all_orders = order_service.get_all_orders()
for order in order_service.get_all_orders():
    print(order)

#print(order_service.get_order("10"))

""" for order in order_service.get_customer_orders("300"):
    print(order) """

order_service.change_order("3", Order("3","20181208","20190404","20200404","400","GP302"))

print("changed orders")
for order in order_service.get_all_orders():
    print(order)

print(order_service.delete_order("5"))

print("deleted orders")
for order in order_service.get_all_orders():
    print(order)

order_service.write_db_to_file()
