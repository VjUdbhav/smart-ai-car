from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    db = mysql.connector.connect(host="localhost", user="udbhavvj", password="Udbhavvj2006", database="smartcar")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM detections ORDER BY timestamp DESC")
    data = cursor.fetchall()
    return render_template("index.html", data=data)

app.run(debug=True)
