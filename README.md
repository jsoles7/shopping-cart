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
- sendgrid <br />
- environms <br />


## Installation:

Fork the repo and clone it to your desktop. <br />
Navigate to the file from the commandline: <br />
```sh
cd shopping-cart/ <br />
```

## Setting up the Environment:
conda create -n shopping-env python=3.7 # (first time only) <br />
conda activate shopping-env <br />
<br />
Proceed to download the following packages <br />
```sh
pip install -r requirements.txt
```
<br />
Make sure to configure your env to fit the required variables: <br />
- Sendgrid API KEY <br />
- Sendgrid API TEMPLATE <br />
- An email address to use for sending and receiving emailed recepits <br />
- Local tax rate <br />

## The `sendgrid` Package


The `sendgrid` package provides  emailing capabilities via the [SendGrid Email Delivery Service](https://sendgrid.com/solutions/email-api/). :mailbox_with_mail: :envelope:

# Installation

From within a virtual environment, install `sendgrid`, if necessary:

```sh
pip install sendgrid==6.0.5
```

First, [sign up for a free account](https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then [create an API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

To setup the usage examples below, store the API Key value in an environment variable called `SENDGRID_API_KEY`. Also set an environment variable called `MY_EMAIL_ADDRESS` to be the email address you just associated with your SendGrid account (e.g. "johndoe@gmail.com").


## Usage:
Run the recommendation script: <br />
- python shopping_cart.py  <br />

The commandline will ask you to enter product identifiers. <br />
Following this, the program will output a receipt, create a .txt file for the receipt,
and send a receipt via email. <br />
It will provide a subtotal, tax value, and total cost. <br />


## Testing

Run the test(s):

```sh
pytest
```


## Code Climate Software Check:
<a href="https://codeclimate.com/github/jsoles7/shopping-cart/maintainability"><img src="https://api.codeclimate.com/v1/badges/b8180925c174866084e1/maintainability" /></a>


