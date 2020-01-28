# shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

#date and time requirements
from datetime import datetime
now = datetime.now()

#user inputs

#define local variable
user_input = ""
input_list = []
subtotal = 0

#run user input while loop until DONE
while (user_input != "DONE"):
    user_input = input("Please input a product identifier: ")

    #append numeric input into the list
    if user_input != "DONE":
        user_input_int = int(user_input)
        input_list.append(user_input_int)


#interface output
#print super market details 
print("---------------------------------")
print("PUBLIX SUPER MARKET")
print("WWW.PUBLIX.COM")
print("---------------------------------")
#print out the current date and time 
print("CHECKOUT AT:", now.strftime("%Y-%m-%d %I:%M %p"))
print("---------------------------------")
print("SELECTED PRODUCTS:")

#run nested for loops in order to print the receipt
for x in input_list:
    
    #define local variables
    product_id = ""
    product_price = 0

    #run for loop to find name and price
    for p in products:
        #if statement to find right product
        if x == p["id"]:
            product_id = p["name"]
            product_price = p["price"]
    
    #print the line item
    print(" ...", product_id.title(), f"(${format(product_price, '.2f')})")

    #keep a running total
    subtotal += product_price

print("---------------------------------")
#print subtotal
print("SUBTOTAL:", f"${format(subtotal, '.2f')}")

#tax + total calculations
tax_total = .0875 * subtotal

print("TAX:", f"${format(tax_total, '.2f')}")

total_price = tax_total + subtotal
print("TOTAL:", f"${format(total_price, '.2f')}")

print("---------------------------------")
print("THANK YOU FOR SHOPPING WITH US TODAY!")
print("CHECK OUT OUR WEBSITE OR CALL US AT 305-586-7219 FOR DELIVERY ORDERS!")
print("---------------------------------")