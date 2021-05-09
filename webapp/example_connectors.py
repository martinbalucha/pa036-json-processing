import json
import time
import ijson

from psycopg2.extras import Json, execute_values
from backend.connectors.mongodb import MongoDbConnector
from backend.connectors.postgres_connector import PostgreSqlConnector


# jsonified_data_for_postgres = Json(file_data)


# Mongo
def mongo_connection(data):
    """
    You don't have to create database beforehand, it will be created automatically. Just make sure MongoDB is installed.
    :param data:
    :return:
    """
    conn = MongoDbConnector()
    my_client = conn.connector(host='localhost', port=27017)
    mydb = my_client["test"]
    mycol = mydb["invoices_table"]

    start = time.time()

    print("MongoDB Insert example: ")
    x = mycol.insert_one(data)
    end = time.time()
    my_client.close()

    print(end - start)


# Postgres
def postgres_connection():
    """
    Postgres must be install and you HAVE TO create database manually.

    :param data:
    :return:
    """
    print("PGSQL Insert example: ")

    psql_conn = PostgreSqlConnector()
    c = psql_conn.connector(host='localhost', port=5432, db_name='postgres', username='postgres', password='admin')
    cur = c.cursor()
    # start = time.time()
    # cur.execute("INSERT into invoice (data) VALUES (%s)", [data])
    # c.commit()
    # end = time.time()
    #
    # print(end - start)
    return cur


cursor = postgres_connection()
with open('webapp/data/fake_invoices.json', encoding='utf-8') as f:
    items = ijson.items(f, "item")
    counter = 0
    json_array = []
    for item in items:
        json_array.append(item)
        if counter == 10:
            break
        counter += 1
    execute_values(cursor,
                   "INSERT INTO invoice (data) VALUES %s",
                   json_array)



# TODO If you change the order of execution (if mongo runs first), it crashes. We must fix this.

# mongo_connection(file_data)
