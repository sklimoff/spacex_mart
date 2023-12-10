import logging

import backoff
from config import config
from psycopg2 import OperationalError, connect


@backoff.on_exception(backoff.expo, (OperationalError,))
def wait_for_pg() -> None:
    connect(config.get_postgres_dsn())


if __name__ == '__main__':
    logging.info('Waiting for PostgreSQL to start...')
    wait_for_pg()
    logging.info('PostgreSQL started.')
