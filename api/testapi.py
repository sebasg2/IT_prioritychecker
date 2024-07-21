import requests
import pymysql
from datetime import datetime

def test_priority():
    url = "http://localhost:8888/priority"
    prompt = "The computer turns on but then turns off 10 seconds later"
    params = {"prompt": prompt}  # Correctly format params as a dictionary
    response = requests.get(url, params=params)
    data = response.json()
    assert "priority" in data
    print("Priority:", data["priority"])

def print_database_contents():
    # Database connection configuration
    username = "admin"
    password = "sg1515eg"
    host = "database-2.cbm2c84euy0d.eu-north-1.rds.amazonaws.com"
    port = 3306
    database = "it_prioritydb"

    # Connect to MySQL
    db = pymysql.connect(
        host=host,
        user=username,
        password=password,
        port=port,
        database=database,
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM incident')
        records = cursor.fetchall()
        print("Database Contents:")
        for record in records:
            print(record)
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

if __name__ == "__main__":
    print_database_contents()
