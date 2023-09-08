# 🛒 Ecom-API
Our E-Commerce API serves as the backend for our online store, providing a comprehensive set of features for users to:

Browse and search for products
Add items to a shopping cart
Place and manage orders
Check product availability
Contact our store
This README provides essential information for developers looking to integrate with our API, including authentication methods, available endpoints, request and response examples, error handling, and more.

## ✨Features

<ul>
  <li>Product Management: Access product catalog, retrieve product details, and check product availability.</li>
  <li>Order Management: Place new orders, retrieve order history, and track order statuses.</li>
  <li>Contact Store: Send inquiries and messages to our store.</li>
  <li>Authentication: Secure endpoints with various authentication methods for user access control.</li>
</ul>

## 📦 Endpoints
Let's make some calls to our endpoint.
Call our endpoints - Here are the requests we can make to our new endpoints.

> This retrieves the auth token for **your_username**

curl -X POST -F 'username=**your_username**' -F 'password=**your_password**' http://api:8000/api-token-auth/

http post http://api:8000/api-token-auth/ username=**your_username** password=**your_password**


> This will retrieve all items

curl -X GET -H 'Authorization: Token **your_token**' http://api:8000/item/

http http://api:8000/item/ 'Authorization: Token **your_token**'


> This will retreive a single item

curl -X GET -H 'Authorization: Token **your_token**' http://api:8000/item/**your_item_uuid**/

http http://api:8000/item/**your_item_uuid**/ 'Authorization: Token **your_token**' 

> This retrieve all orders

curl -X GET -H 'Authorization: Token **your_token**' http://api:8000/order/

http http://api:8000/order/ 'Authorization: Token **your_token**'

> This will place an order for item id = **your_item_uuid** quantity = 1

curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Token **your_token**' -d '{"item": "**your_item_uuid**", "quantity": "1"}' http://api:8000/order/

http http://api:8000/order/ 'Authorization: Token **your_token**' item="**your_item_uuid**" quantity="1"


> This get order id = **your_order_uuid**

curl -X GET -H 'Authorization: Token **your_token**' http://api:8000/order/**your_order_uuid**/

http http://api:8000/order/**your_order_uuid**/ 'Authorization: Token **your_token**'

> This will create a contact request

curl -X POST -H "Content-type: application/json" -d '{"name": "Prateek Thakur", "message": "Hello There", "email":"prateekthakur272@gmail.com"}' 'http://api:8000/contact/'

http http://api:8000/contact/ name="Prateek Thakur" message="Hello There" email="prateekthakur272@gmail.com"


Or try these endpoints in Postman
