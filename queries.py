from connection import *
from app import *
from flask_cors import CORS,cross_origin

mydb=connect_db()
cursor=mydb.cursor()

def signupq(name, email_id,hashed_password, contact,roles):
    query = "INSERT INTO users ( Name, Email_ID, password ,Contact, roles) VALUES (%s, %s, %s,%s,%s);"
    values = ( name, email_id,hashed_password, contact,roles)
    cursor.execute(query, values)
    mydb.commit()
    return jsonify({"role":"error"})