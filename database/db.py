import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def init_db():
    # 1. Connect to PostgreSQL using psycopg2.connect(DATABASE_URL)
    # 2. Open 'database/schema.sql' and read its contents
    # 3. Use cursor.execute() to run the SQL commands
    # 4. Commit changes and close the connection
    pass

if __name__ == "__main__":
    init_db()