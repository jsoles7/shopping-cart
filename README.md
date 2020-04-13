## The project
Python project focused on creating a groceries purchases processor and receipt builder.


## Prerequisites:
- Anaconda 3.7 <br />
- Python 3.7 <br />
- Pip

## Required Python Packages & Modules:
- datetime <br />
- dotenv <br />
- os <br />
- pandas <br />
- sendgrid <br />
- environms <br />


## Installation:

Fork the repo and clone it to your desktop. <br />
Navigate to the file from the commandline: <br />
- cd shopping-cart/ <br />

## Setting up the Environment:
conda create -n shopping-env python=3.7 # (first time only) <br />
conda activate shopping-env <br />
<br />
Proceed to download the following packages <br />
- pip install requirements.txt
<br />
Make sure to configure your env to fit the required variables: <br />
- Sendgrid API KEY <br />
- Sendgrid API TEMPLATE <br />
- An email address to use for sending and receiving emailed recepits <br />
- Local tax rate <br />


## Usage:
Run the recommendation script: <br />
- python shopping_cart.py  <br />

The commandline will ask you to enter product identifiers. <br />
Following this, the program will output a receipt, create a .txt file for the receipt,
and send a receipt via email. <br />
It will provide a subtotal, tax value, and total cost. <br />




