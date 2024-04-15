import mysql.connector
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
db_config = {
    "user": "",
    "password": "",
    "host": "localhost",
    "database": "users",
}


def run_insert(user):
    try:
        cnx = mysql.connector.connect(**db_config)
        cnx.autocommit = True
        cursor = cnx.cursor(dictionary=True)
        sql = (
            "INSERT INTO user (provider_id, name, username, email) "
            "VALUES (%(provider_id)s, %(name)s, %(username)s, %(email)s);"
        )
        params = {
            "provider_id": user["provider_id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
        }
        cursor.execute(sql, params)
        if cnx.is_connected():
            cursor.close()
            cnx.close()
    except Exception:
        pass


def run_update(id, user):
    try:
        cnx = mysql.connector.connect(**db_config)
        cnx.autocommit = True
        cursor = cnx.cursor(dictionary=True)  # Returns data in name: value pairs
        sql = (
            "UPDATE user "
            "SET provider_id = %(provider_id)s, "
            "name = %(name)s, "
            "username = %(username)s, "
            "email = %(email)s "
            "WHERE id = %(id)s;"
        )
        params = {
            "provider_id": user["provider_id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "id": id,
        }
        cursor.execute(sql, params)
        if cnx.is_connected():
            cursor.close()
            cnx.close()
    except Exception:
        pass


def read_api():
    users = []
    feed_data = []
    try:
        results = requests.get(API_URL)
        if results.status_code != 200:
            raise Exception(
                f"Request did not complete correctly {results.status_code}: {results.content}"
            )
        feed_data = results.json()
    except Exception:
        exit()

    for feed_user in feed_data:
        user = {}
        # We'd hopefully be using a documented API, as the following code can throw errors if
        # one of the fields isn't in the feed.  If undocumented, or unsure, its safer to write
        # user.name = feed_user.get("name", "default value")
        # which will return whatever is set as the default value
        # if the item isn't populated in the feed
        user["name"] = feed_user["name"]
        user["provider_id"] = feed_user["id"]
        user["username"] = feed_user["username"]
        user["email"] = feed_user["email"]
        users.append(user)
    return users


def save_data(users):
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor(dictionary=True)  # Returns data in name: value pairs
    for user in users:
        sql = "SELECT id FROM user WHERE provider_id = %(provider_id)s"
        params = {"provider_id": int(user["provider_id"])}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        if cursor.rowcount == 0:
            run_insert(user)
        elif cursor.rowcount == 1:
            run_update(rows[0]["id"], user)
        else:
            raise Exception(f"Multiple rows returned for provider id: {user['provider_id']}")
    if cnx.is_connected():
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    users = read_api()
    save_data(users)
