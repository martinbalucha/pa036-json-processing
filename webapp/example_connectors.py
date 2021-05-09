import json
import time
import ijson

from psycopg2.extras import execute_values
from backend.connectors.mongodb import MongoDbConnector
from backend.connectors.postgres_connector import PostgreSqlConnector


# Mongo
def mongo_connection():
    """
    You don't have to create database beforehand, it will be created automatically. Just make sure MongoDB is installed.
    :return:
    """
    conn = MongoDbConnector()
    my_client = conn.connector(host='localhost', port=27017)
    mydb = my_client["test"]
    mycol = mydb["invoices_table"]
    return mycol


# Postgres
def postgres_connection():
    """
    Postgres must be install and you HAVE TO create database manually.
    :return:
    """
    print("PGSQL Insert example: ")

    psql_conn = PostgreSqlConnector()
    c = psql_conn.connector(host='localhost', port=5432, db_name='postgres', username='postgres', password='admin')
    c.set_client_encoding('UTF8')
    cur = c.cursor()
    return c, cur


def load_json_array(number_of_rows: int):
    """
    Lorem ipsum

    :param number_of_rows: Number of rows
    :return: Loaded json array
    """
    with open('webapp/data/fake_invoices_no_decimal.json', encoding='utf-8') as f:
        items = ijson.items(f, "item")
        counter = 0
        json_array = []
        for item in items:
            json_array.append(item)
            if counter == number_of_rows - 1:
                break
            counter += 1
        return json_array


con, cur = postgres_connection()
mongo_col = mongo_connection()

# TODO: Code below would be in for loop (?)
json_array_loaded = load_json_array(100)  # TODO: parametrize?

print("Inserting to postgresql...")
start = time.time()
execute_values(cur, "INSERT INTO invoice (data) VALUES %s", [[json.dumps(item, ensure_ascii=False)] for item in json_array_loaded])
con.commit()
end = time.time()
print(f"Insert time: {end-start}")

print("Inserting to postgresql jsonb...")
start = time.time()
execute_values(cur, "INSERT INTO invoice_binary (data) VALUES %s", [[json.dumps(item, ensure_ascii=False)] for item in json_array_loaded])
con.commit()
end = time.time()
print(f"Insert time: {end-start}")

print("Inserting to mongodb...")
start = time.time()
mongo_col.insert_many(json_array_loaded)
end = time.time()
print(f"Insert time: {end-start}")
