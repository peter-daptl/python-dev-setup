import pprint

import mysql.connector

db_config = {
    "user": "",
    "password": "",
    "host": "localhost",
    "database": "users",
}


def read_data():
    cnx = mysql.connector.connect(**db_config)
    with cnx.cursor(dictionary=True) as cursor:
        query = "SELECT id, provider_id, name, username, email FROM user;"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows


if __name__ == "__main__":
    pprint.pp(read_data())
