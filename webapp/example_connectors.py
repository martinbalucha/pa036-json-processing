import json
import time

from psycopg2.extras import Json
from backend.connectors.mongodb import MongoDbConnector
from backend.connectors.postgres_connector import PostgreSqlConnector


with open('webapp/data/invoice_example.json') as f:
    file_data = json.load(f)[0]

jsonified_data_for_postgres = Json(file_data)

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

def postgres_connection(data):
    """
    Postgres must be install and you HAVE TO create database manually.

    :param data:
    :return:
    """
    print("PGSQL Insert example: ")

    psql_conn = PostgreSqlConnector()
    c = psql_conn.connector(host='localhost', port=5432, db_name='postgres', username='', password='')
    cur = c.cursor()
    start = time.time()
    cur.execute("INSERT into invoices (invoices_json) VALUES (%s)", [data])
    c.commit()
    end = time.time()

    print(end - start)

# TODO If you change the order of execution (if mongo runs first), it crashes. We must fix this.
postgres_connection(jsonified_data_for_postgres)
mongo_connection(file_data)
