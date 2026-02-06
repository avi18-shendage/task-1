from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    user = request.form['username']
    pwd = request.form['password']
    con = sqlite3.connect("ecommerce.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users VALUES (?,?)", (user,pwd))
    con.commit()
    con.close()
    return "Registered"

@app.route('/order', methods=['POST'])
def order():
    return "Order Saved"

app.run(debug=True)
