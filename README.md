# 🛍️ Django Cart API

This is a Django REST Framework-based backend for managing a simple shopping cart with user authentication, product management, and cart item operations using JWT authentication.
📁 Project Structure


├── cart/ # Cart and Product models
├── api/ # API views, URLs, and serializers
├── manage.py
├── requirements.txt
└── README.md


## Installation
### Step - 1
#### Clone the project
``` git clone https://github.com/mdrahamtansari123/cart_system.git```
### Step - 2
#### Create Virtualenvironment
``` virtualenv env```
### Step - 3
#### Activate virtualenv
``` source env/Scripts/activate```
### Step - 4
#### Install all depedancies

``` pip install -r requirements.txt``` or ``` make install```
=======
``` pip install -r requirements.txt``` or ``` make install```

### Step - 5
#### Initial set up
``` make set-up``` or
### step - 6
'''' python manage.py makemigrations
'''' python manage.py migrate

```python manage.py createsuperuser ```
### Step - 7
#### runserver
``` make runserver``` or
```python manage.py runserver ```
### Step - 8
#### API documentaion URL
- Swagger :- http:1270.0.1:8000/swagger/

## 🚀 Features

- User login with JWT (username:- admin, password:- Admin@123)
- Product management (CRUD)
- Add Product 


✅ Features to Implement
 Cart Features to Implement
Add item to cart

Remove item from cart

Update item quantity

Clear all items from cart

Calculate total cart price

 Endpoint                          Description                              

 `/api/cart/`            GET     List all cart items for the current user 
 `/api/cart/`            POST    Add item to cart                         
 `/api/cart/<item_id>/`  PUT     Update item quantity                     
 `/api/cart/<item_id>/`  DELETE  Remove item from cart                    
 `/api/cart/clear/`      DELETE  Clear all cart items                     
 `/api/cart/total/`      GET     Get total cart price                     





