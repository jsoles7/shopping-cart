# shopping_cart.py

#from pprint import pprint

#packages import
import pandas as pd
import os
from dotenv import load_dotenv
from environs import Env

#process the ENV file 
env = Env()
env.read_env()

#date and time requirements
from datetime import datetime
now = datetime.now()

#products dictionary... not really used due to CSV
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

# TODO: write some Python code here to produce the desired output



#importing the data from the CSV file in an OS friendly way
#read in CSV
csv_filepath = os.path.join(os.path.dirname(__file__), "products.csv")
product_data = pd.read_csv(csv_filepath)

#convert CSV to dictionary
product_data.to_dict()

#user inputs

#define local variable
user_input = ""
input_list = []
subtotal = 0
id_list = []
x = 0
TAX_RATE = env.float('TAX_RATE')



#a list for the email component 
products_list = []


#run user input while loop until DONE
while (user_input != "DONE"):
    user_input = input("Please input a product identifier, or 'DONE' if there are no more: ")


    #append numeric input into the list
    if user_input != "DONE" and (user_input.isdigit() == 1):
        user_input_int = int(user_input)
        if user_input_int > len(products):
            print("Hey, are you sure that product identifier is correct? Please try again!\n")
        else:
            input_list.append(user_input_int)
    elif (user_input.isdigit() == 0) and user_input != "DONE":
        print("Hey, are you sure that product identifier is correct? Please try again!\n")


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
    for index, row in product_data.iterrows():

        row_dict = row.to_dict()
        #if statement to find right product (if identifier doesn't exist, it is ignored)
        if x == row["id"]:
            product_id = row["name"]
            product_price = row["price"]
            #take the dictionary line item 
            s = row.to_dict()
            #append this item
            products_list.append(s)
            #print the line item
            print(" ...", product_id.title(), f"(${format(product_price, '.2f')})")

    
    

    #keep a running total
    subtotal += product_price

print("---------------------------------")
#print subtotal
print("SUBTOTAL:", f"${format(subtotal, '.2f')}")

#tax + total calculations
tax_total = TAX_RATE * subtotal

#output tax
print("TAX:", f"${format(tax_total, '.2f')}")

#calculations for total
total_price = tax_total + subtotal

#output total
print("TOTAL:", f"${format(total_price, '.2f')}")
print("---------------------------------")
print("THANK YOU FOR SHOPPING WITH US TODAY!")
print("CHECK OUT OUR WEBSITE OR CALL US AT 305-586-7219 FOR DELIVERY ORDERS!")
print("---------------------------------")
print("")
print("")

#Save the receipt to a file

#define file name
file_name = str(now.strftime("%Y-%m-%d-%I-%M")) 

#write in the items to the file
with open(file_name, "w") as file:

    file.write("SELECTED PRODUCTS: \n")
    file.write("CHECKOUT AT: ")
    file.write(now.strftime("%Y-%m-%d %I:%M %p"))
    file.write("\n")
    #use a for loop to write the selected products and their prices
    for p in products_list:
        file.write("Product: ")
        file.write(p["name"])
        file.write(";  Price: ")
        #create a local variable for price
        price = p["price"]

        file.write(f"${format(price, '.2f')}")
        file.write("\n")

    #output other essential items of the receipt - e.g. tax and totals
    file.write("SUBTOTAL: ")
    file.write(f"${format(subtotal, '.2f')}")
    file.write("\n")
    file.write("TAX: ")
    file.write(f"${format(tax_total, '.2f')}")
    file.write("\n")
    file.write("TOTAL: ")
    file.write(f"${format(total_price, '.2f')}")
    file.write("\n")

    #output ending message for organization 
    file.write("\n")
    file.write("--- END ---")
    file.write("\n")

#close the file
file.close()


#email to receipt to the client

#the code below is taken from prof. Rossetti's format for emailing content - this has been slightly adjusted to fit the
#variables and parameters of this code
#NOTE: this is mostly his code

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID")
MY_ADDRESS = os.environ.get("EMAIL")
SUBJECT = 'Your receipt from Publix'


client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=SUBJECT)
print("MESSAGE:", type(message))

message.template_id = SENDGRID_TEMPLATE_ID

#create some variables to send in the email
email_price = f"${format(total_price, '.2f')}"

message.dynamic_template_data = {
    "total_price_usd": email_price,
    "human_friendly_timestamp": now.strftime("%d-%m-%Y %I:%M %p"),
    "products":products_list
} # or construct this dictionary dynamically based on the results of some other process :-D

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)