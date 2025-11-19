# database.py
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="HOST",         # your custom server IP
        port=0000,           # your custom Port
        user="User",         # your MySQL username
        password="Password", # your MySQL Password
        database="DB"        # your MySQL DataBase
    )

def setup_database():
    conn = connect_db()
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) UNIQUE,
        password VARCHAR(100),
        role VARCHAR(50)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        restaurant_name VARCHAR(100),
        food_item VARCHAR(100),
        quantity INT,
        status VARCHAR(20) DEFAULT 'available',
        claimed_by_ngo VARCHAR(100)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ngo_name VARCHAR(100),
        food_item VARCHAR(100),
        quantity INT,
        status VARCHAR(20) DEFAULT 'pending',
        fulfilled_by_restaurant VARCHAR(100)
    )
    """)

    conn.commit()
    conn.close()