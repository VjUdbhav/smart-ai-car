import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="udbhavvj",
    password="Udbhavvj2006",
    database="smartcar"
)

cursor = db.cursor()

def save_detection(type, confidence):
    query = "INSERT INTO detections (type, confidence) VALUES (%s, %s)"
    cursor.execute(query, (type, confidence))
    db.commit()
