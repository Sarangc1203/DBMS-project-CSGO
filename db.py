import psycopg2
import config


class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = config.DATABASE_HOST
        self.username = config.DATABASE_USERNAME
        self.password = config.DATABASE_PASSWORD
        self.port = config.DATABASE_PORT
        self.dbname = config.DATABASE_NAME
        self.conn = None

        print(f'Path: {config.PATH}')
        print("Database obj created!")
        print(f'Host={self.host}')

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as e:
                # LOGGER.error(e)
                print(e)
                raise e
            finally:
                # LOGGER.info('Connection opened successfully.')
                print('Connection opened successfully.')

    def execute_query(self, query):
        """Run a SQL query to select rows from table."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            cur.close()
            return records

