from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import Bcrypt
from connection import *
from queries import *


app = Flask(__name__)
cors = CORS(app,origins= "*")


###########################################################
#                           LOGIN                         #
###########################################################
@app.route('/login', methods=['POST'])
def pm_login():
    data = request.get_json()
    Email_ID = data['email_id']
    Password = data['password']
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM Users WHERE Email_ID=%s"
    values = (Email_ID,)
    cursor.execute(query, values)
    users = cursor.fetchone()

    if not users:
        return jsonify({"role": "Invalid Email"})
    else:
        flag=True
        query = "SELECT * FROM Users WHERE Password=%s"
        values = (Password,)
        cursor.execute(query,values)
        users = cursor.fetchone()
        if not users:
            return jsonify ({404, 'Resource not found'})
        else:
            flag2=True
        if flag==flag2==True:
            return jsonify({"Return": "login sucessfull"})
    
###########################################################
#                           SIGNUP                        #
###########################################################
cors = CORS(app,origins= "*")
bcrypt=Bcrypt(app)
@app.route('/add_user', methods=['POST'])
def add_user():
        data = request.get_json()
        name = data['name']
        email_id = data['email_id']
        contact = data['contact']
        roles = data['roles']


        import smtplib
        import random

        def send_otp_email(receiver_email, otp):
            sender_email = "pratik@infobellit.com"  # Replace with your email address
            password = "mzygirleuqcwzwtk"  # Replace with your email password

            message = f"Subject: login credentials for Project Management Tool\n\n Your Username is your email.\nYour password is: {otp}"

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

        def generate_otp(length=6):
            digits = "0123456789abcdefghijklmnopqrstuvwxyz"
            otp = ""
            for _ in range(length):
                otp += random.choice(digits)

            return otp

        # Example usage
        email = email_id  # Replace with the recipient's email address

        otp = generate_otp()
        send_otp_email(email, otp)
        print("OTP sent successfully!")


        # Hash the password
        hashed_password = bcrypt.generate_password_hash(otp).decode('utf-8')

        cursor = mysql.connection.cursor()
        return signupq(name, email_id,hashed_password, contact,roles)
     
                



if __name__ == "__main__":
    app.run(debug=True)
