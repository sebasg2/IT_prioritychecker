import requests
import pymysql
from datetime import datetime

def test_priority():
    # Define la URL del endpoint y el prompt de prueba
    url = "http://localhost:8888/priority"
    prompt = "The computer turns on but then turns off 10 seconds later"
    params = {"prompt": prompt}  # Formatea correctamente los parámetros como un diccionario
    response = requests.get(url, params=params)
    data = response.json()
    assert "priority" in data  # Verifica que la respuesta contenga la clave "priority"
    print("Priority:", data["priority"])

def print_database_contents():
    # Configuración de la conexión a la base de datos
    username = "youruser"
    password = "yourpassword"
    host = "yourhost"
    port = 3306
    database = "it_prioritydb"

    # Conectar a MySQL
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
        # Imprimir el contenido de la base de datos
        for record in records:
            print(record)
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        # Cerrar cursor y conexión a la base de datos
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

if __name__ == "__main__":
    # Ejecutar la función de prueba y la función para imprimir el contenido de la base de datos
    test_priority()
    print_database_contents()
