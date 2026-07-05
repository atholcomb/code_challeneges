#!/usr/bin/python3
# written by: atholcomb
# expensive_orders.py
# Write a function that returns all orders which cost strictly more than amount

def expensive_orders(some_dict, amount):
    result = dict()    

    for key, value in some_dict.items():
        if value > amount:
            result[key] = value

    return result

print(expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000))
print(expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000))
print(expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40))
