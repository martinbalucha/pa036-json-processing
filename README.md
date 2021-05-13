# PA036 JSON Processing
> Performance of JSON processing in MongoDB and PostgreSQL databases

## Project goals
* Understand the differences in JSON processing in MongoDB and PostgreSQL databases
* Measure JSON processing performance on queries of both databases

## Project description
The main use case of the project is the evaluation of databases performance, which stores invoice data in JSON/JSONB formats.
Application’s business logic consist of recording and evaluating the performance of both PostgreSQL and MongoDB when processing invoices in JSON format.
For outputting performance of both databases, a simple web interface is created.

## Prerequisities
> Python in version >= 3.8

Once installed, you should be able to create virtual Python environment and enrich it with necessary dependencies stored in `requirements.txt` file:

```
python -m venv .env
.env\Scripts\activate.bat
pip install -r requirements.txt
```

Furthermore, you need to have PostgreSQL 13.2 and MongoDB installed. The Postgres database that will be used has to have two tables - *invoice* and *invoice_binary*. Both tables have attribute *id* of type *bigserial*. Additionally, both tables have the attribute *data*. In the first case, its type is *json*, in the second case it is *jsonb*. The MongoDB collection has to be called *invoice*. Connection details for can be specified in the file *config.ini*.

The datasource can be downloaded from the following [link](https://owncloud.cesnet.cz/index.php/s/lsBm7VZPGWnmKVA?fbclid=IwAR178voaf80haGoxTTSrCYNzA5ks70JOZSsXsYGqWMioNmovMO84be69_og)

In PyCharm, select the desired interpreter:
> \pa036-json-processing\.env\Scripts\python.exe
 
Finally, select script path to app.py and run the script.

Note: it is needed to have at least 16 GB RAM for the purposes of inserting 1M records due to the JSON loading
