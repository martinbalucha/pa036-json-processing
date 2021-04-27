import psycopg2
from backend.connectors.connector_interface import ConnectorInterface


class PostgreSqlConnector(ConnectorInterface):
    """
    Implementation of the ConnectorInterface for the connection to a PostgreSQL database
    """

    def connector(self, host: str, port: int, username: str = None, password: str = None, **kwargs):
        db_name = kwargs.get("db_name")
        connection = psycopg2.connect(host=host, dbname=db_name, port=port, user=username, password=password)
        return connection
