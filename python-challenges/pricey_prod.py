#!/usr/bin/python3
# written by: atholcomb
# pricey_prod.py
# You will be given a dictionary with various products and their respective prices. 
# Return a list of the products with a minimum price of 500 in descending order.

def pricey_prod(some_dict):
    result = []

    for key, value in some_dict.items():
        if value > 499:
            result.append(key)

    return result

print(pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}))
print(pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}))
print(pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}))
