import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    # Connect to PostgreSQL using psycopg2.connect(DATABASE_URL)
    try:
        conn = psycopg2.connect(DATABASE_URL)
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    with open("database/schema.sql", "r") as f:
        cursor.execute(f.read())

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()