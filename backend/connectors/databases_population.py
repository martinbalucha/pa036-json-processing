import json
from pathlib import Path
from backend.connectors.mongodb import MongoDbConnector

# open example invoice json file
from backend.connectors.postgres_connector import PostgreSqlConnector
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

json_path = Path(__file__).resolve().parent.joinpath('..', '..', 'webapp', 'data', 'invoice_example.json')
with open(json_path) as json_file:
    file_data = json.load(json_file)

# create instance of MongoDbConnector class
mongodb_instance = MongoDbConnector()

# connect to the local instance of database
with mongodb_instance.connector(host="mongodb://localhost", port=27017) as my_connector:
    # create database and collection
    my_database = my_connector['my_database']
    my_collection = my_database['invoice']

    # insert json data
    my_collection.insert_one(file_data[0])

    # print data stored in the collection
    for item in my_collection.find():
        print(item)

with open(json_path) as json_file:
    file_data_ = json.load(json_file)

postgres_instance = PostgreSqlConnector()
# MB: Connection string for a database created locally on my machine. PostgreSQL database cannot be created in memory
# as far as I know
with postgres_instance.connector(host="localhost", username="postgres", password="", db_name="postgres", port=5432) as connector:
    cursor = connector.cursor()
    cursor.execute("INSERT INTO test_table (test) VALUES(3)")
    cursor.execute(f"INSERT INTO test_table(json_test_column) VALUES('{json.dumps(file_data_[0])}')")
    connector.commit()
    cursor.close()