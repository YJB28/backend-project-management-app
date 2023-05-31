from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import Bcrypt
from connection import *
from queries import *


app = Flask(__name__)
cors = CORS(app,origins= "*")

@app.route('/')
def home():
    return '<h1>Welcome Team :To the POC YJB...11</h1>'

# Route for user signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']

    # Create a MySQL connection
    connection = connect_db()
    cursor = connection.cursor()

    # Insert user data into the "User" table
    query = "INSERT INTO User (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    connection.commit()

    # Close the MySQL connection
    cursor.close()
    connection.close()

    return jsonify({"message": "User signup successful"})

# Route for getting all users
@app.route('/users', methods=['GET'])
def get_users():
    # Create a MySQL connection
    connection = connect_db()
    cursor = connection.cursor()

    # Retrieve all users from the "User" table
    query = "SELECT * FROM User"
    cursor.execute(query)
    users = cursor.fetchall()

    # Close the MySQL connection
    cursor.close()
    connection.close()

    # Format the users data
    user_list = []
    for user in users:
        user_data = {
            'id': user[0],
            'name': user[1],
            'email': user[2]
        }
        user_list.append(user_data)

    return jsonify({"users": user_list})


###########################################################
#                           LOGIN                         #


@app.route('/login', methods=['POST'])
def pm_login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    cursor = connect_db().cursor()

    # Retrieve user from the "User" table based on email
    query = "SELECT * FROM User WHERE email = %s"
    values = (email,)
    cursor.execute(query, values)
    user = cursor.fetchone()

    if not user:
        return jsonify({"error": "Invalid Email"})

    stored_password = user[2]

    if bcrypt.check_password_hash(stored_password, password):
        return jsonify({"message": "Login successful..using hashing"})
    else:
        return jsonify({"error": "Invalid Password"})


###########################################################
# @app.route('/login', methods=['POST'])
# def pm_login():
#     data = request.get_json()
#     Email_ID = data['email_id']
#     Password = data['password']
#     cursor = mysql.connection.cursor()
#     query = "SELECT * FROM Users WHERE Email_ID=%s"
#     values = (Email_ID,)
#     cursor.execute(query, values)
#     users = cursor.fetchone()

#     if not users:
#         return jsonify({"role": "Invalid Email"})
#     else:
#         flag=True
#         query = "SELECT * FROM Users WHERE Password=%s"
#         values = (Password,)
#         cursor.execute(query,values)
#         users = cursor.fetchone()
#         if not users:
#             return jsonify ({404, 'Resource not found'})
#         else:
#             flag2=True
#         if flag==flag2==True:
#             return jsonify({"Return": "login sucessfull"})
    
# ###########################################################
# #                           SIGNUP                        #
# ###########################################################
# cors = CORS(app,origins= "*")
# bcrypt=Bcrypt(app)
# @app.route('/add_user', methods=['POST'])
# def add_user():
#         data = request.get_json()
#         name = data['name']
#         email_id = data['email_id']
#         contact = data['contact']
#         roles = data['roles']


#         import smtplib
#         import random

#         def send_otp_email(receiver_email, otp):
#             sender_email = "pratik@infobellit.com"  # Replace with your email address
#             password = "mzygirleuqcwzwtk"  # Replace with your email password

#             message = f"Subject: login credentials for Project Management Tool\n\n Your Username is your email.\nYour password is: {otp}"

#             with smtplib.SMTP("smtp.gmail.com", 587) as server:
#                 server.starttls()
#                 server.login(sender_email, password)
#                 server.sendmail(sender_email, receiver_email, message)

#         def generate_otp(length=6):
#             digits = "0123456789abcdefghijklmnopqrstuvwxyz"
#             otp = ""
#             for _ in range(length):
#                 otp += random.choice(digits)

#             return otp

#         # Example usage
#         email = email_id  # Replace with the recipient's email address

#         otp = generate_otp()
#         send_otp_email(email, otp)
#         print("OTP sent successfully!")


#         # Hash the password
#         hashed_password = bcrypt.generate_password_hash(otp).decode('utf-8')

#         cursor = mysql.connection.cursor()
#         return signupq(name, email_id,hashed_password, contact,roles)
     
                



if __name__ == "__main__":
    app.run(debug=True)
