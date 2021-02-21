# zaruratapp

# create users for login

url: POST   http://127.0.0.1:5000/register

payload: { "username": "person1", "password": "person1" }

# generating jwt to access dashboard

url :  http://127.0.0.1:5000/auth 

payload: { "username": "person1", "password": "person1" }

Sample Output : {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTM4OTA5MzgsImlhdCI6MTYxMzg5MDYzOCwibmJmIjoxNjEzODkwNjM4LCJpZGVudGl0eSI6M30.5kG4K-fppLptgEMIxCpN8LbYGaJWcvXbpN4WyTSkJhM"
}

# inserting product details

url : POST http://127.0.0.1:5000/dashboard

payload: { "product_name": "pen", "price": "5" }

# get product details

url: GET http://127.0.0.1:5000/dashboard
