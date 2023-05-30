from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True

# MySQL configuration
app.config["MYSQL_HOST"] = "your_mysql_host"
app.config["MYSQL_USER"] = "your_mysql_username"
app.config["MYSQL_PASSWORD"] = "your_mysql_password"
app.config["MYSQL_DB"] = "your_mysql_database"

# Initialize MySQL
mysql = MySQL(app)

# Enable CORS
CORS(app)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {
        "id": 1,
        "isbn": "9781593279509",
        "title": "Eloquent JavaScript, Third Edition",
        "subtitle": "A Modern Introduction to Programming",
        "author": "Marijn Haverbeke",
        "published": "2018-12-04T00:00:00.000Z",
        "publisher": "No Starch Press",
        "pages": 472,
        "description": "JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
        "website": "http://eloquentjavascript.net/"
    },
    {
        "id": 2,
        "isbn": "9781491943533",
        "title": "Practical Modern JavaScript",
        "subtitle": "Dive into ES6 and the Future of JavaScript",
        "author": "Nicolás Bevacqua",
        "published": "2017-07-16T00:00:00.000Z",
        "publisher": "O'Reilly Media",
        "pages": 334,
        "description": "To get the most out of modern JavaScript, you need learn the latest features of its parent specification, ECMAScript 6 (ES6). This book provides a highly practical look at ES6, without getting lost in the specification or its implementation details.",
        "website": "https://github.com/mjavascript/practical-modern-javascript"
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>POC-Backend</h1>
                <p>A Flask API implementation for book information.</p>'''

@app.route('/api/v1/books/all', methods=['GET'])
def api_all():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    return jsonify(books)

@app.route('/api/v1/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)


@app.route('/api/v1/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (id,))
    results = cur.fetchall()
    cur.close()

    return jsonify(results)

@app.route("/api/v1/books", methods=['POST'])
def api_insert():
    book = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO books (id, isbn, title, subtitle, author, published, publisher, pages, description, website) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (book['id'], book['isbn'], book['title'], book['subtitle'], book['author'], book['published'], 
                 book['publisher'], book['pages'], book['description'], book['website']))
    mysql.connection.commit()
    cur.close()
    return "Success: Book information has been added."

@app.route("/api/v1/books/<id>", methods=['DELETE'])
def api_delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return "Success: Book information has been deleted."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
