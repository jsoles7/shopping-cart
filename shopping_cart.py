# shopping_cart.py

#from pprint import pprint

#packages import
import csv
import os
from dotenv import load_dotenv
from environs import Env



#function to convert into USD format
def to_usd(my_price):
    """
        This function is used to convert float numbers passed to it to a formatted price in traditional US format.

        Source: Prof. Rossetti's In class Example.

        @param: the my_price variable is a price input that comes as a float (e.g. 13.98570) and 
                represents a variable that is supposed to be converted to a price format.

    """
    return "${0:,.2f}".format(my_price)

#function to find product once given a product ID
def find_product(id, product_list):
    """
        This function is used to find the matching product when given a product ID and a dictionary of products.
        It makes use of list comprehension in order to find the right product and return.

        @param: this function has two variables: the first variable is a product ID code that is an integer;
                the second variable is the product_list which is a dictionary variable that contains all the products.

    """
    same_product = [p for p in product_list if str(p["id"]) == str(id)]
    product = same_product[0]
    return product


if __name__ == "__main__":

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

    product_data = []

    #importing the data from the CSV file in an OS friendly way
    csv_filepath = os.path.join(os.path.dirname(__file__), "products.csv")
    with open(csv_filepath) as f:
        reader = csv.DictReader(f)
        product_data = [d for d in reader]



    #define local variable
    user_input = ""
    input_list = []
    subtotal = 0
    id_list = []
    x = 0
    TAX_RATE = env.float('TAX_RATE')


    #a list for the email component 
    products_list = []


    #PART 1: Collect the Data


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


    #PART 2: Output the Data

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


    for inp in input_list:

        #define local variables
        product_id = ""
        product_price = 0

        #run the fuction
        matching_product = find_product(inp, product_data)
        product_id = matching_product["name"]
        product_price = float(matching_product["price"])

        print(" ...", product_id.title(), to_usd(product_price))

        #keep a running total
        subtotal += product_price
        #add to email list
        products_list.append(matching_product)

    print("---------------------------------")
    #print subtotal
    print("SUBTOTAL:", to_usd(subtotal)) 

    #tax + total calculations
    tax_total = TAX_RATE * subtotal

    #output tax
    print("TAX:", to_usd(tax_total))

    #calculations for total
    total_price = tax_total + subtotal

    #output total
    print("TOTAL:", to_usd(total_price))
    print("---------------------------------")
    print("THANK YOU FOR SHOPPING WITH US TODAY!")
    print("CHECK OUT OUR WEBSITE OR CALL US AT 305-586-7219 FOR DELIVERY ORDERS!")
    print("---------------------------------")
    print("")
    print("")



    #PART 3: Save the receipt to a file

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
            file.write(to_usd(float(p["price"])))
            file.write("\n")

        #output other essential items of the receipt - e.g. tax and totals
        file.write("SUBTOTAL: ")
        file.write(to_usd(subtotal))
        file.write("\n")
        file.write("TAX: ")
        file.write(to_usd(tax_total))
        file.write("\n")
        file.write("TOTAL: ")
        file.write(to_usd(total_price))
        file.write("\n")

        #output ending message for organization 
        file.write("\n")
        file.write("--- END ---")
        file.write("\n")

    #close the file
    file.close()


    #PART 4: Email to receipt to the client
    answer = input("Would the customer like an emailed receipt (write NO if not)? ")
    answer = answer.upper()

    if answer != "NO":

        

        #the code below is taken from Prof. Rossetti's format for emailing content - this has been slightly adjusted to fit the
        #variables and parameters of this code
        #NOTE: this is mostly his code

        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        load_dotenv()

        #get customer email
        print("")
        CUST_ADDRESS = input("If the customer would like an emailed recepit, please enter their email: ")
        print("")
        print("")
        print("")


        SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
        SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID")
        MY_ADDRESS = os.environ.get("EMAIL")
        SUBJECT = 'Your receipt from Publix'


        client = SendGridAPIClient(SENDGRID_API_KEY)
        print("CLIENT:", type(client))

        message = Mail(from_email=MY_ADDRESS, to_emails=CUST_ADDRESS, subject=SUBJECT)
        print("MESSAGE:", type(message))

        message.template_id = SENDGRID_TEMPLATE_ID

        #create some variables to send in the email
        email_price = to_usd(total_price)

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