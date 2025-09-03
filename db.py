import mysql.connector

DB_NAME = "b7mhanlonjp5hn8uiuoy"

def get_db_connection(db_required=True):
    conn = mysql.connector.connect(
        host="b7mhanlonjp5hn8uiuoy-mysql.services.clever-cloud.com",
        user="uh6jh8knswi9fpie",         
        password="YRRGCafTISFAdSJpqTeG"
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    conn.commit()
    conn.close()

    if db_required:
        return mysql.connector.connect(
            host="b7mhanlonjp5hn8uiuoy-mysql.services.clever-cloud.com",
            user="uh6jh8knswi9fpie",
            password="YRRGCafTISFAdSJpqTeG",
            database=DB_NAME
        )
    return None


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
