import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="portfolio_user",
            password="salman2006/",
            database="portfolio_db"
        )
        return conn
    except Error as e:
        print(f"Database connection failed: {e}")
        return None