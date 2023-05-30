import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {
        "id": 1,
        "isbn":"9781593279509",
        "title":"Eloquent JavaScript, Third Edition",
        "subtitle":"A Modern Introduction to Programming",
        "author":"Marijn Haverbeke",
        "published":"2018-12-04T00:00:00.000Z",
        "publisher":"No Starch Press",
        "pages":472,
        "description":"JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
        "website":"http://eloquentjavascript.net/"
    },
    {
        "id": 2,
        "isbn":"9781491943533",
        "title":"Practical Modern JavaScript",
        "subtitle":"Dive into ES6 and the Future of JavaScript",
        "author":"Nicolás Bevacqua",
        "published":"2017-07-16T00:00:00.000Z",
        "publisher":"O'Reilly Media",
        "pages":334,
        "description":"To get the most out of modern JavaScript, you need learn the latest features of its parent specification, ECMAScript 6 (ES6). This book provides a highly practical look at ES6, without getting lost in the specification or its implementation details.",
        "website":"https://github.com/mjavascript/practical-modern-javascript"
    }
]
@app.route('/', methods=['GET'])
def home():
    return '''<h1>VLib - Online Library</h1>
                <p>A flask api implementation for book information.   </p>'''
@app.route('/api/v1/books/all', methods=['GET'])
def api_all():
    return jsonify(books)@app.route('/api/v1/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."results = []
    for book in books:
        if book['id'] == id:
            results.append(book)return jsonify(results)
@app.route("/api/v1/books",  methods = ['POST'])
def api_insert():
    book = request.get_json()
    books.append(book)
    return "Success: Book information has been added."
@app.route("/api/v1/books/<id>", methods=["DELETE"])
def api_delete(id):
    for book in books:
        if book['id'] == int(id):
            books.remove(book)
    return "Success: Book information has been deleted."
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)




# from flask import Flask, render_template, request, url_for, flash, jsonify
# from werkzeug.utils import redirect
# from flask_mysqldb import MySQL
# import mysql.connector
# import os

# app = Flask(__name__)

# # Get MySQL database configuration from environment variables
# db_host = os.environ.get('DB_HOST')
# db_user = os.environ.get('DB_USER')
# db_password = os.environ.get('DB_PASSWORD')
# db_name = os.environ.get('DB_NAME')

# # Connect to MySQL database
# mydb = mysql.connector.connect(
#     host=db_host,
#     user=db_user,
#     password=db_password,
#     database=db_name
# )

# cursor = mydb.cursor()

# mysql = MySQL(app)

# @app.route('/login', methods=['POST'])
# def pm_login():
#     try:
#         data = request.get_json()
#         Email_ID = data['email_id']
#         Password = data['password']
#         cursor = mydb.cursor()
#         query = "SELECT * FROM Users WHERE Email_ID=%s"
#         values = (Email_ID,)
#         cursor.execute(query, values)
#         users = cursor.fetchone()

#         if not users:
#             return jsonify({"role": "Invalid Email"})
#         else:
#             flag=True
#         query = "SELECT * FROM Users WHERE Password=%s"
#         values = (Password,)
#         cursor.execute(query,values)
#         users = cursor.fetchone()
#         if not users:
#             return jsonify({"role": "Invalid Password"})
#         else:
#             flag2=True
#         if flag==flag2==True:
#             return jsonify({"Return": "login sucessfull"})


        
     
                

#     except KeyError as e:
#         # Handle missing key in the request data
#         return jsonify({"error": "Missing key in request data: " + str(e)}), 400

#     except mysql.connector.Error as err:
#         # Handle MySQL database-related errors
#         return jsonify({"error": "Database error: " + str(err)}), 500

#     except Exception as e:
#         # Handle any other unexpected exceptions
#         return jsonify({"error": "An error occurred: " + str(e)}), 500



# if __name__ == "__main__":
#     app.run(debug=True)
