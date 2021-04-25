from pymongo import MongoClient

from backend.connectors.connector_interface import ConnectorInterface


class MongoDbConnector(ConnectorInterface):
    """
    CLass implementing the ConnectorInterface class and creating the connector instance to the MongoDB database
    """

    def connector(self, host: str, port: int, username: str = None, password: str = None, **kwargs):
        """
        This method should be implemented while trying to create the connector to MongoDB database
        :param host: MongoDB database host address
        :param port: MongoDB database port number
        :param username: Username to be used for authentication
        :param password: Password to be used for authentication
        :return: Connector instance to the MongoDB database
        """
        mongodb_connector = MongoClient(
            host=host,
            port=port,
            username=username,
            password=password
        )

        return mongodb_connector
