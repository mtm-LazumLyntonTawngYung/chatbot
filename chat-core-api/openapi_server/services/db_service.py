import logging
import os
from contextlib import contextmanager

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from openapi_server.variables import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, INSTANCE_CONNECTION_NAME


class ChienowaNetDbService:

    def __init__(self):
        url = self.get_db_url_by_environment()
        self.engine = create_engine(url, echo=False, poolclass=NullPool)
        self.Session = sessionmaker(bind=self.engine, autocommit=False)

    @staticmethod
    def get_db_url_by_environment():
        url = 'mysql+pymysql://'
        url += '@' + INSTANCE_CONNECTION_NAME + ':3306/'
        url += DATABASE_NAME
        return url

    @contextmanager
    def start_session(self, commit=False):
        session = None
        try:
            session = self.Session()
            try:
                yield session
                if commit:
                    session.commit()
            except Exception as e:
                logging.info(e)
                session.rollback()
                raise
        finally:
            if session is not None:
                session.close()
