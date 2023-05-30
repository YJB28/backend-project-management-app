from flask import Flask, render_template, request, url_for, flash, jsonify
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)
mydb = mysql.connector.connect(
    host="mysqldb-service",
    user="root",
    password="root",
    database="pmt",
  
)
cursor = mydb.cursor()


mysql = MySQL(app)
@app.route('/login', methods=['POST'])
def pm_login():
    try:
        data = request.get_json()
        Email_ID = data['email_id']
        Password = data['password']
        cursor = mydb.cursor()
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
            return jsonify({"role": "Invalid Password"})
        else:
            flag2=True
        if flag==flag2==True:
            return jsonify({"Return": "login sucessfull"})


        
     
                

    except KeyError as e:
        # Handle missing key in the request data
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        return jsonify({"error": "An error occurred: " + str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)